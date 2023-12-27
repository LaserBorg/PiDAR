import wifi
import ssl
import socketpool
import adafruit_requests
import microcontroller

# private function
def get_socketpool(ssid, password):
    wifi.radio.connect(ssid, password)
    pool = socketpool.SocketPool(wifi.radio)
    return pool
    
# main function
def start_session(ssid, password):
    pool = get_socketpool(ssid, password)
    session = adafruit_requests.Session(pool, ssl.create_default_context())
    return session

# adafruit example
def print_response(session, url="https://www.adafruit.com/api/quotes.php"):
    try:
        response = session.get(url)
        response_test = response.text
        print("Text Response: ", response_test)
        response.close()
        return response_test    
    except:
        except Exception as e:
        print("Error:\n", str(e))
        print("Resetting microcontroller!")
        microcontroller.reset()
