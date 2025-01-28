from model.da.da import DataAccess
from model.entity import Ticket, Logger


def save(name, title , description,time,date,state):
    try:
        ticket = Ticket(name, title , description,time,date,state)

        ticket_da = DataAccess(Ticket)
        ticket_da.save(ticket)
        Logger.info(f"Member {ticket} Saved")
        return True, ticket
    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False, f"{e}"


def edit(id, name, title , description,time,date,state):
    try:
        ticket = Ticket(name, title , description,time,date,state)
        ticket.id = id

        member_da = DataAccess(Ticket)
        member_da.edit(ticket)
        Logger.info(f"Member {ticket} Edited")
        return True, ticket
    except Exception as e:
        Logger.error(f"{e} - Not Edited")
        return False, f"{e}"


def remove_by_id(id):
    try:
        ticket_da = DataAccess(Ticket)
        ticket = ticket_da.remove_by_id(id)

        Logger.info(f"Member {ticket} Removed")
        return True, ticket
    except Exception as e:
        Logger.error(f"{e} - Not Removed")
        return False, f"{e}"


def find_all():
    try:
        ticket_da = DataAccess(Ticket)
        ticket_list = ticket_da.find_all()
        Logger.info(f"Member FindALL")
        return True,ticket_list
    except Exception as e:
        Logger.error(f"{e} - FindALL")
        return False, f"{e}"

def find_by_id(id):
    try:
        ticket_da = DataAccess(Ticket)
        ticket = ticket_da.find_by_id(id)
        if ticket:
            Logger.info(f"Ticket FindById {id}")
            return True, ticket
        else:
            raise ValueError("No Ticket Found")
    except Exception as e:
        Logger.error(f"{e} - FindById {id}")
        return False, f"{e}"

