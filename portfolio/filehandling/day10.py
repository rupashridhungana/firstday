#sabile le share garne obkect lai class varaibale vanainaxa


#inheritance
# parent ko property child le acess garyo vane 
# class parent:
#     class child(parent):



# types of inhritance 
# single inhritance =single inherit from one parent only
# multiple inheritance
# multilabeling
# class GrandFather:
# class father(grand father):
# class child(GrandFather,father)


# multilevel
#  class GrandFather:
# class father(grand father):
# class child(GrandFather,father)

# hierarchical inheritance
#  class GrandFather:
# class father(grand father):
# class child(father)





#  this is a parent class single inheritance
# class father:
#     surname ='Dhungana'
#     def break_fast(self):
#         print("we eat fruits")
#     def family_surname(self):
#         print(f"we have surname '{self.surname}'.")


        
    
# # this is a child class
# class child(father):
#     def break_fast(self):
#         print("we eat pizza")
#     pass
# ch1=child()
# ch2=child()
# print(ch1.break_fast())
# print(ch1.surname)
# print(ch2.surname)
# print(ch1.family_surname())




# class Grandparent:
#     def eye_color(self):
#         print("eye color is blue")
#     pass
# class parent(Grandparent):
#     def hair_color(self):
#         print("hair color is pink")
#     def eye_color(self):
#         print("my eye is black color")
#     pass
# class child(parent):
#     def height(self):
#         print("my height is 5.2")
#     def hair_color(self):
#         print("my hair is blue")

#     pass
# c1=child()
# c1.eye_color()
# c1.hair_color()
# c1.height()



# multiple inheritance

# class father:
#     def driving(self):
#      print("good at driving")
#      def cocking(self):
#         print("good at coking")
#      pass
    

# class mother:
#     def cocking(self):
#      print("good at coking")
#     def driving(self):
#      print("ok in driving")

#      pass
# class child(father,mother):
#     pass

# child1=child()
# child1.driving()
# child1.cocking()




# class parent:
#     surname='dhungana'
#     def land(self):
#         print("we have 100 ropani")  
    
#     pass
# class child1(parent):

#     pass
# class child2(parent):
#     pass

# c1=child1()
# c1.land()
# print(c1.surname)
# c2=child2()
# c2.land()
# print(c2.surname)


class parent:
    def launch(self):
        print("we eat  samosa")
    pass
class child(parent):
    def launch(self):
        super().launch()
        print("we eat  momo")
    pass

child=child()
child.launch()





