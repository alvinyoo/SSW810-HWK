select CWID, Name from Instructors
where CWID = '98763';

select Dept, count(*) as cnt
from Instructors group by Dept

select Grade, count(*) as cnt
from Grades group by Grade;

select s.Name, s.CWID, s.Major, g.Course, g.Grade
from Students s
    left join Grades g on s.CWID = g.StudentCWID

select s.Name, g.Course, g.Grade
from Students s
    left join Grades g on s.CWID = g.StudentCWID
where Course = 'SSW 810'

select i.CWID, i.Name, i.Dept, g.Course, count(*) as student_num
from Instructors i
left join Grades g on i.CWID = g.InstructorCWID
group by g.Course, g.InstructorCWID
order by g.InstructorCWID