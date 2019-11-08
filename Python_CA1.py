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
            
            try:
                student_course_number=int(student_course_number)
                except:
                    print('student_course_number must be a number with no decimal points')
                    continue
                    
                    if not len(str(student_id)) == 8:
                print('student_id must be 8 digits long')
                # breaks loop and restarts loop
                continue
                    

            print('student_course_number: ' + str(student_course_number))

    def show_menu(self):
     
        
        while selected_option != '1' and selected_option != '2':
          
            print('Press 1 to execute the add() function')
            print('Press 2 to execute the show_all_records() function')
           
            selected_option = input('Enter your option > ')
            print('You have selected: ' + selected_option)
            if selected_option == '1':
            
                self.add()
            else selected_option == '2':
                self.show_all_records()
                
        

         

def main():
    s = StudentRecords([
        [7, 'A. McStudent', 'A1234567'],
        [9, 'B. McStudent', 'B1234567'],
        [2, 'C. McStudent', 'C1234567'],
        [1, 'D. McStudent', 'E1234567'],
        [3, 'E. McStudent', 'F1234567'],
        [8, 'F. McStudent', 'G1234567'],
        [5, 'G. McStudent', 'H1234567'],
        [6, 'H. McStudent', 'I1234567'],
        [99999999, 'I. McStudent', 'D1234567']
])
    s.show_menu()
