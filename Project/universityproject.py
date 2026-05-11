while True:
 
    print("  *****INFO UNIVERSITY***** ")

    print("\t1. Details ")
    print("\t2. Admission ")
    print("\t3. Student Profile ")
    print("\t4. Fees Structure ")
    print("\t5. upload result ")
    print("\t6. Result ")

    x=int(input("Enter Your Choice:"))
    match x:
        case 1:
            print("You Enter Details:\n")
            detail=input("Detail for UG or PG :").lower()
            if detail=="ug":
                print("* THERE ARE FIVE STREAMS IN UG ENTER SUBJECT NAME: ")
                print(" 1. BA \n 2. BSC \n 3. BCA \n 4. B.COM \n 5. B.TECH")
                ugcource=input("YOU ARE INTRESTED IN WHICH COURCE:").lower()
                match ugcource:
                    case "ba":
                        paragraph="""A Bachelor of Arts (BA) is a 3-year (sometimes 4-year under NEP)  
                        Key Highlights of BA 
                        CourseFull Form: Bachelor of Arts
                        Duration: 3 Years (divided into 6 semesters)
                        Eligibility: 10+2 from a recognized board (Arts, Science, or Commerce)
                        Admission: Based on merit or entrance exams (e.g., CUET, IPU CET)
                        Average Fees: INR 10,000 – INR 20,000 (public) to higher in private colleges
                        Average Salary: INR 4 – 6 LPA"""
                        print(paragraph)
                 
                    case "bsc":
                        paragraph=""" A Bachelor of Computer Science (BCS) is a 3-year undergraduate program focusing on computer applications, programming, and software development. The curriculum covers core subjects like C++, Java, Data Structures, Operating Systems, Database Management (DBMS), and Networking, offering a balance of theory and practical skill development."""
                        print(paragraph)
                    case "bca":
                        paragraph=""" BCA (Bachelor of Computer Applications) subjects focus on software development, programming languages (C, C++, Java, Python), database management, data structures, and computer networks over 6 semesters. The curriculum blends theoretical knowledge with practical lab work (35–40 total subjects), including web tech and software engineering."""  
                        print(paragraph)    
                    case "b.com":
                        paragraph="""B.Com (Bachelor of Commerce) is a 3-year undergraduate degree focusing on accounting, finance, taxation, and management. Core subjects include Financial Accounting, Business Law, Economics, and Cost Accounting. The curriculum is structured to provide a strong base for careers in banking, auditing, and corporate management """
                        print(paragraph)  
                    case "b.tech":
                        paragraph=""" B.Tech subjects comprise a blend of foundational engineering sciences (physics, math, programming) in the first year, followed by specialized core subjects, labs, and electives from the second year onwards. The 4-year (8-semester) curriculum focuses on practical training, projects, and domain-specific knowledge to prepare for technical roles."""
                        print(paragraph) 
                    case _:
                        print("Invalid Choice")
            else:
                print("* THERE ARE FOUR STREAMS IN PG ENTER SUBJECT NAME:")
                print(" 1. MCA \n 2. MBA \n 3.MSC \n 4. M.TECH") 
                              
                pgcource=input(" YOU WANT TO KNOW ABOUT:").lower()
                match pgcource:
                    case "mca":
                        paragraph="""Master of Computer Applications (MCA) is a 2-year postgraduate program focusing on advanced computer science, application development, and computational theory. Core subjects typically include Programming in Python/Java/C++, Data Structures, Operating Systems, Database Management Systems (DBMS), Software Engineering, and Computer Networks. The curriculum is structured to blend theoretical knowledge with practical coding skills, often including AI, Cloud Computing, and web technologies in later semesters.Core Subjects (Common Across Semesters)Programming Fundamentals: Python Programming, Object-Oriented Programming (Java/C++), C Programming.Systems and Architecture: Operating Systems, Computer Organization and Architecture, System Software.Data and Networking: Data Structures and Algorithms, Database Management Systems (DBMS), Computer Networks, Advanced Database Management Systems.Software Development: Software Engineering, Web Technologies (PHP/HTML/CSS), Web Application Development Frameworks.Mathematics and Theory: Mathematical Foundations of Computer Science, Optimization Techniques, Theory of Computation, Probability and Linear Algebra.Advanced Topics and ElectivesArtificial Intelligence (AI): Machine Learning, Deep Learning, Digital Image Processing.Data and Cloud: Cloud Computing, Big Data Analytics, Data Analytics and R Programming.Security: Cryptography and Network Security, Cyber Security.Management: Agile Project Management and Testing, Research Methodology.Practical and Project WorkData Structures Lab (C/C++).RDBMS Lab (SQL).Java Programming Lab.Machine Learning Lab in Python.Major and Mini Projects (final semesters).Typical Semester-wise StructureSemester 1: Python Programming, Data Structures, RDBMS, Software Engineering, Math for Computing.Semester 2: Java Programming, Computer Networks, Operating Systems, Machine Learning, Web Development.Semester 3: Cloud Computing, Data Analytics, Algorithms, Electives (Mobile App Development/Deep Learning).Semester 4: Major Projects, Technical Seminars, and Industrial Training.MCA Course Details: Subjects, Syllabus and EligibilityCloud Computing. Mobile Computing. Systems Management. These specialisations enhance industry relevance and align academic learnin...Jain UniversityMCA Courses: Subjects and Syllabus in Details - Vignan OnlineMathematical Foundations of Computer Science: Covers logic, set theory, and algorithms. Database Management System: Focuses on SQL...Vignan OnlineMCA Syllabus 2026: Subjects List, Semester-wise ... - Shiksha.comTable_title: MCA Syllabus 2025 Table_content: header: | MCA 1st Sem Subjects 2025 | | row: | MCA 1st Sem Subjects 2025: Python Pro...Shiksha.comShow all """
                        print(paragraph)
                    case "mba":
                        paragraph="""MBA subjects for 2026 cover foundational business management, leadership, and analytical skills, typically split into core subjects (first year) and specialization electives (second year). Key core subjects include Finance, Marketing, Organizational Behavior, Operations, and Strategy, while specialization tracks cover topics like Data Analytics, Digital Marketing, and Fintech """
                        print(paragraph)
                    case "msc":
                        paragraph=""" M.Sc (Master of Science) subjects are specialized, two-year postgraduate programs focusing on advanced theoretical and practical knowledge in science and technology fields. Key specializations include Physics, Chemistry, Mathematics, Biotechnology, Data Science, and Computer Science, typically covering core, elective, and research-based laboratory work"""
                        print(paragraph)
                    case "m.tech":
                        paragraph="""M.Tech (Master of Technology) subjects are highly specialized based on the chosen engineering branch, focusing on advanced theoretical knowledge, research, and industrial applications. Core subjects include advanced engineering mathematics, specialized subjects in Computer Science (AI/ML, Data Science), Electronics (VLSI, Embedded Systems), Mechanical (Thermal, Design), and Civil Engineering (Structural, """
                        print(paragraph)
                    case _:
                        print("Invalid Choice")
                 
        case 2:
            print("*STUDENT ADMISSION:")
            name=input("Enter Your Name:").lower()
            fathername=input("Enter Your Father Name:").lower()
            age=int(input("Enter your age:"))
            userid=input("Enter user id:").lower()
            password=input("Enter password:").lower()
            
            if age<15:
                print("Under age")
            else:
                pass
            stream=input("Enter Your subject:").lower()
            if stream=="Bca" or "bsc" or "b.com" or "ba" or "b.tech" or "mca" or "m.tech" or "mba" or "msc":
                pass
            else:
                print("Envalid choice")
            per=int(input("Enter 12th percentage:"))
            p = "Eligble" if per>65 else "Waiting" if per>60 else "Not Eligble"            #use of inline 
            print("your status",p)
            mobile=int(input("Enter your mobile Number:"))
            email=input("Enter your email id:").lower()
            admissionyear=int(input("Enter admission year:"))
            address=input("Enter your address:")
            
            
            print("Congratulations , Admission Successfully Done")
            
        case 3:
            print("* STUDENT PROFILE")
            id=input("Enter User Id:").lower()
            password1=input("Enter Password:").lower()
            if id==userid:
                if password1==password:
                    print("Name:",name)
                    print("Father name:",fathername)
                    print("Age:",age)
                    print("Stream:",stream)
                    print("Percentage:",per)
                    print("Mobile:",mobile)
                    print("Email:",email)
                    print("Adimission year:",admissionyear)
                    print("Address:",address)
                else:
                    print("Incorrect password !!!")
            else:
                print("Invalid User name")
           
        case 4:
            print("4. FEES STRUCTURE ")
            paragraph="""Establishing a clear fee structure on your website is essential for transparency and building trust with prospective students. Since tuition can vary significantly based on the institution's tier (Government vs. Private) and location, I have prepared a standardized template that reflects current average market rates in India for 2026.You can copy and adapt this table for your site's "Admissions" or "Fee Structure" page.Undergraduate Programs: Annual Fee Structure (Academic Year 2026-27)The following table provides an estimated breakdown of the tuition and registration fees for our primary undergraduate courses.
            Course CategoryDurationAverage Annual Tuition FeeOne-Time Admission FeeTotal (Est. Year 1)
            B.A. (Bachelor of Arts)3 Years₹15,000 – ₹45,000₹5,000₹20,
            000B.Sc. (Bachelor of Science)3 Years₹25,000 – ₹60,000₹7,500₹32,
            500B.Com. (Bachelor of Commerce)3 Years₹20,000 – ₹55,000₹5,000₹25,
            000BCA (Computer Applications)3 Years₹60,000 – ₹1,20,000₹10,000₹70,
            000B.Tech. (Engineering)4 Years₹1,50,000 – ₹3,50,000₹25,000₹1,75,
            000Important Notes for ApplicantsExamination Fees:
              These are typically charged per semester and are not included in the tuition fees mentioned above.Lab & Material Fees: 
              Specifically for B.Sc. and B.Tech. students, additional charges may apply for laboratory maintenance and specialized equipment.Hostel & Mess: For students opting for on-campus housing, these charges are billed separately based on the type of accommodation (Standard/AC).Scholarships: Merit-based scholarships are available for students scoring above 90% in their qualifying examinations.Pro-Tip for your Website: Always include a small disclaimer at the bottom stating: "Fees are subject to change based on university regulations and government norms. Please contact the accounts office for a detailed breakdown."Would you like me to add a section for specific specializations (like AI for B.Tech or Finance for B.Com) to make the list more detailed? """
            print(paragraph)
        
        case 5:
            print("*UPLOAD RESULT")
            trainer=input("Enter Trainer name:").lower()
            pin=int(input("Enter pin:"))
            if trainer=="ajay singh":
                if pin==121212:
                    id=input("Enter student id:")
                    sum=0
                    for i in range(1,5):
                        x=int(input("Enter student marks:"))
                        sum=sum+x
                    result="Pass Excillent:" if sum>=300 else "Pass Good:" if sum>=150 else "Fail:"
                    print("Marks are Successfully Recorded")
                else:
                    print("invalid pin")
            else:
                print("Invalid Trainer ID")                
        case 6:
            print("6.* STUDENT RESULT ")
            id=input("Enter User ID:")
            password1=input("Enter Password:")
            if userid==id:
                if password1==password:
                    print(result,sum)
                else:
                    print("Invaild Password")
            else:
                print("Invalid User ID")
        case 7:
            print("Invalid choice")
            break
        case _:
            print("invalid Choice")
