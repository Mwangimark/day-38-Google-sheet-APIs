from datetime import datetime
import os
from dotenv import load_dotenv
import requests

load_dotenv()

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers ={
    "x-app-id" : os.getenv("APP_ID"),
    "x-app-key": os.getenv("APIKEY")
}

parameters = {
    "query":input("What Exercie did you do today ?"),
    "gender":os.getenv("GENDER"),
    "weight_kg": os.getenv("WEIGHT"),
    "height_cm":os.getenv("HEIGHT"),
    "age" : os.getenv("AGE")
}


header = {
    "Authorization": os.getenv("MYTOKEN")
}

data = requests.post(exercise_endpoint,json=parameters,headers=headers)
result = data.json()
print(result)



# ################################################### step 4 #############################################################
today_date = datetime.now().strftime("%d/%m/%y")
now_time = datetime.now().strftime("%X")

url = os.getenv("url")
for workout in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": workout["user_input"],
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"]
        }
    }

    sheet_response = requests.post(url,json=sheet_inputs,headers=header)
    print(sheet_response.text)


