from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI()


class Exhibit(BaseModel):
    id: int
    name: str
    language: str
    description: Optional[str] = None
    audio_guide_url: Optional[str] = None
    date_created: datetime
    collection_id: int
    


exhibits_db: List[Exhibit] = [
    
    Exhibit(
        id=1,
        name="Carthaginian Art",
        language="en",
        description="The art of the Carthaginians was an eclectic mix of influences and styles.",
        audio_guide_url="audio/audio1.m4a",
        date_created=datetime.now(),
        collection_id=1
    ),
    Exhibit(
        id=2,
        name="Carthaginian Art",
        language="fr",
        description="L'art des Carthaginois était un mélange éclectique d'influences et de styles.",
        audio_guide_url="audio/audio6.m4a",
        date_created=datetime.now(),
        collection_id=1
    ),
    Exhibit(
        id=3,
        name="Carthaginian Art",
        language="ar",
        description="كان فن القرطاجيين مزيجًا انتقائيًا من التأثيرات والأنماط.",
        audio_guide_url="audio/audio11.m4a",
        date_created=datetime.now(),
        collection_id=1
    ),

    
    Exhibit(
        id=4,
        name="Bizerte Lake Mosaic",
        language="en",
        description=(
            "Origin: The Bizerte region (Sidi Abdallah). "
            "Dating: End of IV – beginning of V century A.D. "
            "Materials: Marble, limestone. "
            "A representation of the Bizerte Lake in ancient times. "
            "The mosaic was discovered in a maritime villa in Sidi Abdallah at the Lake of Bizerte."
        ),
        audio_guide_url="audio/audio2.m4a",
        date_created=datetime.now(),
        collection_id=2
    ),
    Exhibit(
        id=5,
        name="Bizerte Lake Mosaic",
        language="fr",
        description=(
            "Origine: La région de Bizerte (Sidi Abdallah). "
            "Datation: Fin du IVe - début du Ve siècle après J.-C. "
            "Matériaux: Marbre, calcaire. "
            "Une représentation du lac de Bizerte dans l'Antiquité. "
            "La mosaïque a été découverte dans une villa maritime à Sidi Abdallah au bord du lac de Bizerte."
        ),
        audio_guide_url="audio/audio7.m4a",
        date_created=datetime.now(),
        collection_id=2
    ),
    Exhibit(
        id=6,
        name="Bizerte Lake Mosaic",
        language="ar",
        description=(
            "الأصل: منطقة بنزرت (سيدي عبد الله). "
            "التأريخ: نهاية القرن الرابع - بداية القرن الخامس الميلادي. "
            "المواد: الرخام والحجر الجيري. "
            "تمثيل لبحيرة بنزرت في العصور القديمة. "
            "تم اكتشاف الفسيفساء في فيلا بحرية بسيدي عبد الله على ضفاف بحيرة بنزرت."
        ),
        audio_guide_url="audio/audio12.m4a",
        date_created=datetime.now(),
        collection_id=2
    ),

    
    Exhibit(
        id=7,
        name="Julius Seigniorial Domain",
        language="en",
        description=(
            "Materials: Clay, marble. "
            "Dating: Beginning of V century A.D. "
            "Origin: Carthage. "
            "Seignior Julius’s wealthy hours. Activities around a big Seigniorial domain in the Carthage suburbs."
        ),
        audio_guide_url="audio/audio3.m4a",
        date_created=datetime.now(),
        collection_id=3
    ),
    Exhibit(
        id=8,
        name="Julius Seigniorial Domain",
        language="fr",
        description=(
            "Matériaux: Argile, marbre. "
            "Datation: Début du Ve siècle après J.-C. "
            "Origine: Carthage. "
            "Les heures fastes de Seignior Julius. Activités autour d'un grand domaine seigneurial dans la banlieue de Carthage."
        ),
        audio_guide_url="audio/audio8.m4a",
        date_created=datetime.now(),
        collection_id=3
    ),
    Exhibit(
        id=9,
        name="Julius Seigniorial Domain",
        language="ar",
        description=(
            "المواد: الطين والرخام. "
            "التأريخ: بداية القرن الخامس الميلادي. "
            "الأصل: قرطاج. "
            "الساعات المزدهرة للسيد يوليوس. الأنشطة حول مجال سيادي كبير في ضواحي قرطاج."
        ),
        audio_guide_url="audio/audio13.m4a",
        date_created=datetime.now(),
        collection_id=3
    ),

    
    Exhibit(
        id=10,
        name="Virgil and the Muses",
        language="en",
        description=(
            "Origin: Sousse. "
            "Dating: Beginning of III century A.D. "
            "Materials: Marble. "
            "This was discovered in a house in Sousse (Hadrumetum). Virgil writing the VIII verse of the Aeneid while being inspired by the muses, Clio and Melpomene."
        ),
        audio_guide_url="audio/audio4.m4a",
        date_created=datetime.now(),
        collection_id=4
    ),
    Exhibit(
        id=11,
        name="Virgil and the Muses",
        language="fr",
        description=(
            "Origine: Sousse. "
            "Datation: Début du IIIe siècle après J.-C. "
            "Matériaux: Marbre. "
            "Ceci a été découvert dans une maison à Sousse (Hadrumetum). Virgile écrivant le VIIIe vers de l'Énéide tout en s'inspirant des muses, Clio et Melpomène."
        ),
        audio_guide_url="audio/audio4.m4a",
        date_created=datetime.now(),
        collection_id=4
    ),
    Exhibit(
        id=12,
        name="Virgil and the Muses",
        language="ar",
        description=(
            "الأصل: سوسة. "
            "التأريخ: بداية القرن الثالث الميلادي. "
            "المواد: الرخام. "
            "تم اكتشاف هذا في منزل في سوسة (هدروميتوم). فيرجيل يكتب الآية الثامنة من الإنيادة بينما يستوحي الإلهام من الموسيقتين، كليو وميلبومين."
        ),
        audio_guide_url="audio/audio14.m4a",
        date_created=datetime.now(),
        collection_id=4
    ),

    # Apollo Citharoedus
    Exhibit(
        id=13,
        name="Apollo Citharoedus",
        language="en",
        description=(
            "Origin: Bulla Regia. "
            "Dating: II century A.D. "
            "Materials: Marble. "
            "A monumental marble statue of Apollo Citharoedus. The divinity is represented while standing up with a nonchalant attitude. "
            "The lightweight posture is accentuated by putting his hand over his head, nudity from the chest to the groin, and by the direction of the drapery which seems to be slipping down. "
            "In fact, Apollo seems to be taunting his opponents such as the Phrygian satyr Marsyas who finished by being skinned alive because he dared to defy him in a musical competition. "
            "The unfortunate rival is indirectly evoked here through a small bas-relief adorning the zither on which the divinity’s left hand rests and which depicts a character sharpening a cutlass."
        ),
        audio_guide_url="audio/audio5.m4a",
        date_created=datetime.now(),
        collection_id=5
    ),
    Exhibit(
        id=14,
        name="Apollo Citharoedus",
        language="fr",
        description=(
            "Origine: Bulla Regia. "
            "Datation: IIe siècle après J.-C. "
            "Matériaux: Marbre. "
            "Une statue monumentale en marbre d'Apollon Citharède. La divinité est représentée debout avec une attitude nonchalante. "
            "La posture légère est accentuée par le fait qu'il met sa main sur sa tête, la nudité de la poitrine à l'aine, et par la direction du drapé qui semble glisser vers le bas. "
            "En fait, Apollon semble narguer ses adversaires tels que le satyre phrygien Marsyas qui a fini par être écorché vif parce qu'il a osé le défier dans une compétition musicale. "
            "Le malheureux rival est évoqué ici indirectement à travers un petit bas-relief ornant la cithare sur laquelle repose la main gauche de la divinité et qui représente un personnage aiguisant un coutelas."
        ),
        audio_guide_url="audio/audio10.m4a",
        date_created=datetime.now(),
        collection_id=5
    ),
  Exhibit(
        id=15,
        name="Apollo Citharoedus",
        language="ar",
        description=(
            "الأصل: بولا ريجيا. "
            "التأريخ: القرن الثاني الميلادي. "
            "المواد: الرخام. "
            "تمثال رخامي ضخم لأبولو كيثارويدوس. يتم تمثيل الإله واقفًا بموقف غير مبالٍ. "
            "الوضعية الخفيفة يتم تعزيزها بوضع يده على رأسه، العري من الصدر إلى العانة، ومن خلال اتجاه الستار الذي يبدو وكأنه ينزلق. "
            "في الواقع، يبدو أن أبولو يتحدى خصومه مثل الساتير الفريغي مارسياس الذي انتهى به الأمر إلى أن يُسُلخ حيًا لأنه تجرأ على تحديه في مسابقة موسيقية. "
            "الخصم التعيس يتم استحضاره بشكل غير مباشر هنا من خلال نقوش بارزة صغيرة تزين القيثارة التي تستند إليها يد الإله اليسرى والتي تصور شخصية تقوم بشحذ سكين."
        ),
        audio_guide_url="audio/audio15.m4a",
        date_created=datetime.now(),
        collection_id=1
    )
]

@app.get("/exhibits/details")
def get_exhibit_details(name: str, language: str):
    """
    Retrieve exhibit details by name and language.
    """
    for exhibit in exhibits_db:
        if exhibit.name.lower() == name.lower() and exhibit.language.lower() == language.lower():
            return {
                "name": exhibit.name,
                "language": exhibit.language,
                "description": exhibit.description,
                "audio_guide_url": exhibit.audio_guide_url
            }
    raise HTTPException(status_code=404, detail=f"Exhibit '{name}' not found in language '{language}'")

@app.get("/exhibits/names")
def get_exhibit_names():
    """
    Retrieve a list of exhibit names.
    """
    exhibit_names = set(exhibit.name for exhibit in exhibits_db)
    return [{"name": name} for name in exhibit_names]


@app.route('/statue/<name>', methods=['OPTIONS'])
def options_statue_info(name):
    statue = statues_data.get(name.lower())
    
    if not statue:
        return jsonify({"error": "Statue not found"}), 404

    
    supported_languages = list(statue['description'].keys())
    return jsonify({
        "name": statue['name'],
        "supported_languages": supported_languages,
        "methods": ["GET", "OPTIONS"]
    }), 200



@app.post("/exhibits/")
async def add_exhibit(exhibit: Exhibit):
    
    return {"message": "Exhibit added successfully!", "exhibit": exhibit}



@app.put("/exhibits/{exhibit_id}")
def update_exhibit(exhibit_id: int, exhibit: Exhibit):
    """
    Update an existing exhibit.
    """
    for i, existing_exhibit in enumerate(exhibits_db):
        if existing_exhibit.id == exhibit_id:
            exhibits_db[i] = exhibit
            return {"message": "Exhibit updated successfully!", "exhibit": exhibit}
    raise HTTPException(status_code=404, detail=f"Exhibit with id {exhibit_id} not found")


class ExhibitNameUpdate(BaseModel):
    name: str

@app.patch("/exhibits/{exhibit_id}")
def update_exhibit_name(exhibit_id: int, exhibit: ExhibitNameUpdate):
    """
    Update the name of an exhibit by ID.
    """
    for exhibit in exhibits_db:
        if exhibit.id == exhibit_id:
            exhibit.name = exhibit.name  
            return {
                "id": exhibit.id,
                "name": exhibit.name,
                "language": exhibit.language,
                "description": exhibit.description,
                "audio_guide_url": exhibit.audio_guide_url,
                "date_created": exhibit.date_created,
                "collection_id": exhibit.collection_id
            }
    raise HTTPException(status_code=404, detail=f"Exhibit with ID {exhibit_id} not found")