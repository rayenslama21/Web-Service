from fastapi import APIRouter

virtualvisit = APIRouter()

virtual_tour_link = "https://www.google.com/maps/@36.8095299,10.1341126,2a,75y,354.25h,46.3t/data=!3m7!1e1!3m5!1sFQS3pKjmKrmXTXKAqZ5ymQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D43.696473677361475%26panoid%3DFQS3pKjmKrmXTXKAqZ5ymQ%26yaw%3D354.2535393288268!7i13312!8i6656?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D"

@virtualvisit.get("/virtual-tour")
def get_virtual_tour():
    return {"virtual_tour_link": virtual_tour_link}