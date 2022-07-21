def get_event_data(event):
    return event.data
def current_user(events):
    events.sort(key=get_event_data)
    machines= {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine]=set()
        if event.type=="login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machines].remove(event.user)
        return machines
def generate_report(machines):
    for machine,users in machines.items():
        if len(users)>0:
          user_list=",".join(users)
          print("{} : {}".format(machines,user_list))