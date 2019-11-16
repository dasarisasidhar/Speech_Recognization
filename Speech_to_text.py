import speech_recognition as sr 

sample_rate = 48000
chunk_size = 2048
recognizer = sr.Recognizer() 
mic_list = sr.Microphone.list_microphone_names() #list of microphones
print("Please select which microphone you want to use to convert speech to text")
for i,microphone_name in enumerate(mic_list):
    print(i,".", microphone_name)  #get all the microphone_name connected to device
while(True):
    with sr.Microphone(device_index = mic_id, sample_rate = sample_rate,  
                       chunk_size = chunk_size) as source: 
        recognizer.adjust_for_ambient_noise(source) 
        print ("Say Something")
        audio = recognizer.listen(source)     
        try: 
            text = recognizer.recognize_google(audio) 
            print ("you said: " + text )   
        except sr.UnknownValueError: 
            print("Google Speech Recognition could not understand audio") 
        except sr.RequestError as e: 
            print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
    print("please click on any key to process next time else press on 1")
    user_input = input()
    if(user_input == "1"):
        break
