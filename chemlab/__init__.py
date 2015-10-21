import sys

__version__ = '0.4.1'

# Setup pyqt API
import sip
try:
    sip.setapi('QDate', 2)
    sip.setapi('QDateTime', 2)
    sip.setapi('QString', 2)
    sip.setapi('QtextStream', 2)
    sip.setapi('Qtime', 2)
    sip.setapi('QUrl', 2)
    sip.setapi('QVariant', 2)
except ValueError as e:
    raise RuntimeError('Could not set API version (%s): did you import PySide directly?' % e)
