from .models import Vps

def test_reinstall(vps: Vps):
    vps.reinstall(vps.template)
