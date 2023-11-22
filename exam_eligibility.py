total_number_of_classes=int(input("Enter total number of classes conducted: "))
total_number_of_attended_classes=int(input("Enter total number of attended classes: "))

attendance_percentage = (total_number_of_attended_classes/total_number_of_classes)*100

if(attendance_percentage>75):
    print(f"Your attendance percentage is {attendance_percentage}%. You can attend the exam")
else:
    print(f"Your attendance percentage is {attendance_percentage}%. You cannot attend the exam")    
    
