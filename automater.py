from selenium import webdriver
import random
import time
    
millisecs = round(time.time() * 3.14)
random.seed(millisecs)

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("--headless")
option.add_argument("disable-gpu")

i = 0
while i < 20:
  browser = webdriver.Chrome(executable_path='./chromedriver', options=option)
  form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdPkvUyug5Vt-EyaPJtkh5ZOBw4rWrvXwjBDthi7BWWCasTMA/viewform"
  browser.get(form_url)

  questions = browser.find_elements_by_class_name("freebirdFormviewerComponentsQuestionBaseRoot")
  submitbutton = browser.find_element_by_class_name("freebirdFormviewerViewNavigationSubmitButton")

  for num, question in enumerate(questions,start = 1):
    textboxes = question.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    radiobuttons = question.find_elements_by_class_name("freebirdFormviewerComponentsQuestionRadioChoice")
    checkboxes = question.find_elements_by_class_name("freebirdFormviewerComponentsQuestionCheckboxChoice")
    
    if len(textboxes) > 0:
        textboxes[0].send_keys("Fill by hand")

    if len(radiobuttons) > 0:
      random_radioButton = random.choice(radiobuttons)
      random_radio_button_index = radiobuttons.index(random_radioButton)
      radiobuttons[radiobuttons.index(random_radioButton)].click()

    if len(checkboxes) > 0:
      random_checkbox = random.choice(checkboxes)
      random_checkbox_index = checkboxes.index(random_checkbox)
      if random_checkbox.is_displayed():
        checkboxes[random_checkbox_index].click()

      choice = random.choice([True, False])
      if choice == True:
          random_checkbox2 = random.choice(checkboxes)
          if random_checkbox2.is_displayed():
            random_checkbox2index = checkboxes.index(random_checkbox2)
            if random_checkbox2index != random_checkbox_index:
              checkboxes[random_checkbox2index].click()

  submitbutton.click()
  browser.close()
  i += 1
  print(i)
else:
  print("Done")

# IGNORE THIS BIT

  # weight = 0
  # height = 0

# def range_switcher(argument):
#   switcher = {
#     8: [63,113],
#     9: [150,198],
#     10: [35,80],
#     14:[16,30],
#     51:[5,25]
#   }
#   value_range = switcher.get(argument, [1,10])
#   return value_range;

# value_range = range_switcher(num)
# input = random.randint(value_range[0], value_range[1])
# if num == 8:
#   weight = input

# if num == 9:
#   height = input

# if num == 10:
#   bmi = round(weight / (height/100)**2, 2)
#   textboxes[0].send_keys(str(bmi))
# else:
#   textboxes[0].send_keys(input)