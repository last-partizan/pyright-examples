def update_historical_traffic(port):
    ...


def start_update_portmap():
    from app.tasks import update_portmap
    update_portmap(None)
