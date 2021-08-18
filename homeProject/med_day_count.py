import datetime

dose_durations = {
    1 : [[6,24]],
    2 : [[6,18],[18,24]],
    3 : [[6,12],[12,18],[18,24]],
}

def extract_and_made_meds():
	meds = []
	with open('meds.txt', 'r') as f:
		texts = f.read()
	texts = texts.split("\n")
	for text in texts:
		text = text.strip()
		med_details = []
		attrs = text.split(",")
		for attr in attrs:
			val = attr.strip()
			if val.isnumeric():
				med_details.append(int(val))
			else:
				med_details.append(val)
		meds.append(med_details.copy())
	meds = [x for x in meds if len(x) == 3]
	return meds



def today_remaining(per_day_dose):
 	global dose_durations
 	now = datetime.datetime.now()
 	passed_hour = int(now.strftime("%H"))
 	taken_doses = 0
 	time_list = dose_durations[per_day_dose]
 	for time in time_list:
 		if time[1] <passed_hour or time[0]<=passed_hour<=time[1]:
 			taken_doses+=1
 		else:
 	  		break 
 	return per_day_dose - taken_doses

def get_days_and_remaining_doses(med):
	  med_name,med_count,per_day_dose = med
	  todays_remaining = today_remaining(per_day_dose)
	  med_count -= todays_remaining
	  tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
	  days_remaining = med_count // per_day_dose
	  dose_remaing = med_count % per_day_dose
	  finishing_date = (tomorrow + datetime.timedelta(days=days_remaining)).strftime("%d-%B-%Y  %A")
	  print(f"{med_name} has {todays_remaining} remaining doses today, will continue untill {finishing_date}, still {dose_remaing} will remain")
  
if __name__ =="__main__":
	meds = extract_and_made_meds()
	for med in meds:
		get_days_and_remaining_doses(med)




