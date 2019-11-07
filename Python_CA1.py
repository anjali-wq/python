class StudentRecords:
    def __init__(self, records):
        self.records = records

   def add(self):
        student_id = 0
        student_id_loop_active = True

        student_full_name = ''
        student_full_name_loop_active = True

        student_course_number = ''
        student_course_number_loop_active = True

        while student_id_loop_active:
            student_id = input('Enter your 8 digit student_id > ')
            # gets array of existing_ids
            existing_ids = [i[0] for i in self.records]

 while student_course_number_loop_active:
            student_course_number = input('Enter 7 digit course number > ')
            if len(student_course_number) == 0:
                print('Please enter a course number')
                continue

  if not len(str(student_course_number)) == 7:
                print('Course number must be 7 digits long')
                continue

            print('student_course_number: ' + str(student_course_number))

    def show_menu(self):
     
        
