from db import Neo4jConnection

conn = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", password="1234@1234")

def create_student(student_id, name, age, department):
    query = """
    CREATE (s:Student {student_id: $student_id, name: $name, age: $age, department: $department})
    RETURN s
    """
    return conn.query(query, parameters={"student_id": student_id, "name": name, "age": age, "department": department})

def get_student(student_id):
    query = """
    MATCH (s:Student {student_id: $student_id})
    RETURN s
    """
    return conn.query(query, parameters={"student_id": student_id})

def update_student(student_id, name, age, department):
    query = """
    MATCH (s:Student {student_id: $student_id})
    SET s.name = $name, s.age = $age, s.department = $department
    RETURN s
    """
    return conn.query(query, parameters={"student_id": student_id, "name": name, "age": age, "department": department})

def delete_student(student_id):
    query = """
    MATCH (s:Student {student_id: $student_id})
    DELETE s
    RETURN COUNT(s) AS count
    """
    result = conn.query(query, parameters={"student_id": student_id})
    return result[0]["count"] > 0

