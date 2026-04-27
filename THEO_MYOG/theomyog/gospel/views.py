from django.shortcuts import render

STATIONS_DATA = {
    1: {
        "title": "Chapter 1: The Labyrinth",
        "bg_img": "gospel/images/chapter1.jpg",
        "location": "Taft Avenue Station",
        "story": "The sun isn't even up, but the journey begins in a maze of half-finished concrete. You walk through narrow, makeshift plywood paths because two multi-billion companies couldn't agree on where their tracks should meet. You are a ghost in their legal battle.",
        "issue": "Corporate Interest vs. Human Movement",
        "metric": "10-Year Connectivity Gap",
        "prophetic_action": "Criticize the 'Station as a Brand'. Proclaim the 'Station as a Sanctuary'—a place designed for people, not for corporate borders.",
        "value": "The Common Good",
        "next": 2
    },
    2: {
        "title": "Chapter 2: The Squeeze",
        "bg_img": "gospel/images/chapter2.jpg",
        "location": "Inside the MRT-3 Coach",
        "story": "The doors hiss shut, pressing your chest against a stranger’s backpack. You aren't a person anymore; you are a 'load factor.' In this metal box, the system has optimized you into a sardine to save on electricity and train deployment.",
        "issue": "Dehumanization for Efficiency",
        "metric": "160% Over-Capacity",
        "prophetic_action": "Criticize the 'Person-as-Cargo' logic. Proclaim the 'Sacredness of Breath'—that every commuter deserves space to exist with dignity.",
        "value": "Human Dignity",
        "next": 3
    },
    3: {
        "title": "Chapter 3: The Physical Trial",
        "bg_img": "gospel/images/chapter3.jpg",
        "location": "Ortigas Avenue Station",
        "story": "You reach your transfer, but the escalator is silent—'Under Maintenance' for the third month. You watch an elderly woman grip the rail, facing the 108-step ascent. Your legs ache, but your heart aches more for those the city has decided to leave behind.",
        "issue": "Able-bodied Infrastructure Bias",
        "metric": "108 Steps (Elevator Uptime: 0%)",
        "prophetic_action": "Challenge the 'Survival of the Fittest' transit model. Proclaim a city that moves at the pace of its slowest member.",
        "value": "Option for the Poor and Vulnerable",
        "next": 4
    },
    4: {
        "title": "Chapter 4: The Stolen Hours",
        "bg_img": "gospel/images/chapter4.jpg",
        "location": "Ortigas Avenue Station (Going Home)",
        "story": "Work is done, but your day is far from over. You stand on the scorching pavement of EDSA in a line that doesn't move. Two hours of your life are 'taxed' away by the queue. These are hours stolen from your family, your sleep, and your soul.",
        "issue": "Temporal Poverty",
        "metric": "120-Minute Wait Time",
        "prophetic_action": "Challenge the 'Normalization of Penance'. Proclaim the 'Right to Rest'—that no worker should pay for their wage with their limited time on earth.",
        "value": "The Dignity of Work",
        "next": 5
    },
    5: {
        "title": "Chapter 5: The Seamless Light",
        "bg_img": "gospel/images/chapter5.jpg",
        "location": "EDSA Walkways to the Doorstep",
        "story": "You finally step off the train, but the 'system' abandons you at the gate. The streets are dark, the sidewalks are broken, and the last mile home feels like a gauntlet. But then, you realize: the Gospel doesn't end at the station. It starts with us building the bridge home.",
        "issue": "Fragmented Responsibility",
        "metric": "Safety Blind Spots",
        "prophetic_action": "Criticize the 'Gate-to-Gate' mindset. Proclaim a 'Seamless Covenant' where the community and state ensure every child and worker reaches their door in peace.",
        "value": "Solidarity",
        "next": None
    }
}

def landing_page(request):
    context = {
        'project_title': 'Delayed Lives',
        'project_tagline': 'An audit of the systems that move us. Journey through five critical bottlenecks...',
        'student_name': 'Amado D. Malhabour Jr. VII',
    }
    return render(request, 'gospel/landing.html')

def station_detail(request, station_id):
    station = STATIONS_DATA.get(station_id)
    if not station:
        return render(request, 'gospel/landing.html')
    # Pass 'id': station_id so the template knows which number it is
    return render(request, 'gospel/station_detail.html', {'station': station, 'id': station_id})