#Graph
#{A : [B,C,D],
# B: [A,E],
# C: [A,D],
# D: [A,C,E],
# E:[B,D]}
#Adjacency matrix
# class Graph:
#   def __init__(self):
#     self.adjacency_list = {}

#   def add_vertex(self, vertex):
#     if vertex not in self.adjacency_list.keys():
#       self.adjacency_list[vertex] = []
#       return True
#     return False
#   def print_graph(self):
#     for vertex in self.adjacency_list:
#       print(vertex, ':', self.adjacency_list[vertex])

# my_graph = Graph()
# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')
# my_graph.add_vertex('E')
# my_graph.add_vertex('F')
# my_graph.print_graph()


#{A:[B,C,D],
#B:[A,E],
#C:[A,D],
#D:[A,C,E],
#E:[B,D]}
#Adjacency list
#{A:[B,C,D],
#B:[A,E],
#C:[A,D],
#D:[A,C,E],
#E:[B,D]}

# class Graph:
#     def __init__(self):
#         self.adjancy_list = {}

#     def add_vertex(self,vertex):
#         if vertex not in self.adjancy_list.keys():
#             self.adjancy_list[vertex]=[]
#             return True
#         return False
    
#     def print_graph(self):
#         for vertex in self.adjancy_list:
#             print(vertex,":",self.adjancy_list[vertex])

#     def add_edge(self, vertex1, vertex2):
#         if  vertex1 in self.adjancy_list.keys() and  vertex2 in self.adjancy_list.keys():
#             self.adjancy_list[ vertex1].append( vertex2)
#             self.adjancy_list[ vertex2].append( vertex1)
#             return True
#         return False  
#     def remove_vertex(self, vertex):
#         if vertex in self.adjacency_list:
#         # Remove this vertex from all other adjacency lists
#            for other_vertex in self.adjacency_list[vertex]:
#             self.adjacency_list[other_vertex].remove(vertex)
#         # Delete the vertex itself
#             del self.adjacency_list[vertex]
#            return True
#         return False




#     def print_graph(self):
#         for vertex in self.adjancy_list:
#             print(vertex, ":", self.adjancy_list[vertex])
      

# my_graph = Graph()
# my_graph.add_vertex("A")
# my_graph.add_vertex("B")
# my_graph.add_vertex("C")
# my_graph.add_vertex("D")
# my_graph.add_vertex("E")

# my_graph.add_edge("A", "B")

# my_graph.add_edge("A", "C")

# my_graph.add_edge("A", "D")

# my_graph.add_edge("B", "A")

# my_graph.add_edge("B", "E")


# my_graph.add_edge("C", "D")

# my_graph.add_edge("D", "E")


# # Print graph
# my_graph.print_graph()
#class Graph:
#   def _init_(self):
#     self.adjacency_list = {}

#   def add_vertex(self, vertex):
#     if vertex not in self.adjacency_list.keys():
#       self.adjacency_list[vertex] = []
#       return True
#     return False
#   def print_graph(self):
#     for vertex in self.adjacency_list:
#       print(vertex, ':', self.adjacency_list[vertex])

# my_graph = Graph()
# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')
# my_graph.add_vertex('E')
# my_graph.add_vertex('F')
# my_graph.print_graph()
# [21:01, 21/05/2026] Annanya.K RBU: class Graph:
#   def _init_(self):
#     self.adjacency_list = {}

#   def add_vertex(self, vertex):
#     if vertex not in self.adjacency_list.keys():
#       self.adjacency_list[vertex] = []
#       return True
#     return False
#   def print_graph(self):
#     for vertex in self.adjacency_list:
#       print(vertex, ':', self.adjacency_list[vertex])

#   def add_edge(self, v1, v2):
#     if v1 in self.adjacency_list.keys() and v2 in self.adjacency_list.keys():
#       self.adjacency_list[v1].append(v2)
#       self.adjacency_list[v2].append(v1)
#       return True
#     return False
  
#   def remove_edge(self, v1, v2):
#     if v1 in self.adjacency_list.keys() and v2 in self.adjacency_list.keys():
#         self.adjacency_list[v1].remove(v2)
#         self.adjacency_list[v2].remove(v1)
#         return True
#     else:
#       print("Edge not found")
#       return False

#   def remove_vertex(self, vertex):
#     if vertex in self.adjacency_list.keys():
#       del self.adjacency_list[vertex]
#       return True
#     else:
#       print("Vertex not found")
#       return False

# my_graph = Graph()
# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')
# my_graph.add_vertex('E')

# my_graph.add_edge('A', 'B')
# my_graph.add_edge('A', 'C')
# my_graph.add_edge('A', 'D')
# my_graph.add_edge('B', 'E')
# my_graph.add_edge('C', 'D')
# my_graph.add_edge('D', 'E')
# my_graph.remove_vertex('E')
# my_graph.remove_edge('A', 'D')

# my_graph.print_graph()


#static method
# '@' is decorator
# class Student:
#     #by using class name we access static method
#     @staticmethod
#     def get_personal_detail(firstname,lastname):
#         print("your personal detail=",firstname,lastname)

#     @staticmethod
#     def contact_detail(mobil_no,rollno):
#         print("your contact detail=",mobil_no,rollno)
# Student.get_personal_detail("Anjali","Patalbansi")
# Student.contact_detail(8620050503,101)

#Garbage collection
#SINGLE LEVEL INHERITANCE
# class College:
#     def college_name(self):
#         print("RBU")
# class Student(College):
#     def student_info(self):
#         print("Name: Anjali Patalbansi")
#         print("Branch: AI")

# obj = Student()
# obj.college_name()
# obj.student_info()

#Multilevel inheritance:

# class College:
#     def college_name(self):
#         print("RBU")

# class Student(College):
#     def student_info(self):
#         print("Name:  Anjali Patalbansi")
#         print("Branch: AI")

# class Exam(Student):
#     def subject(self):
#         print("Subject1: Design Engineering")
#         print("Subject2: Math")
#         print("Subject3: C-Language")

# obj =  Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()

#Multiple Inheritance
# class SubjMarks:
#     Math = int(input("Enter paper marks of math:"))
#     DE = int(input("Enter paper marks of design engineering:"))
#     C= int(input("Enter paper marks of english:"))
#     English = int(input("Enter paper marks of english:"))

# class PractMarks:
#     cpract = int(input("Enter practicals marks of c language:"))

# class Result(SubjMarks,PractMarks):
#     #print("if student pass in both = subject and practical paper then pass")
#     def total(self):
#         if self.Math>=40 and self.DE>=40 and self.C>=40 and self.English>=40 and self.cpract>=20:
#             print("pass")
#         else:
#             print("fail")
# obj = Result()
# obj.total()

#Polymorphism

# class RBI:
#     def home_loan(self):
#         print("Home Loan ROI = 8%")
        

#     def education_loan(self):
#         print("Education loan = 9%")

# class SBI(RBI):
#     def education_loan(self):
#         print("Education loan = 10%")
#         super().education_loan()

# obj = SBI()
# obj.education_loan()

#Constructor Overloading
class RBI:
    def __init__(self):
        print("Parent class constructor")
        


class SBI(RBI):
    def __init__(self):
        print("Child class constructor")
        super().__init__()
        

obj = SBI()



