import random

import mysql.connector
import logging
import random
from mysql.connector import Error

logger = logging.getLogger('candidate_dao')

def getMySQLConnection():
    try:
        connection_config_dict = {
            'user': 'edureka',
            'password': 'edureka',
            'host': '127.0.0.1',
            'port': '3306',
            'database': 'dinasys',
            'raise_on_warnings': True
        }
        connection = mysql.connector.connect(**connection_config_dict)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            logger.info("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            logger.info("You're connected to database: ", record)
        else:
            logger.info("MySQL not connected")
        return connection
    except Error as e:
        logger.info("Error while connecting to MySQL", e)
        print("Error while connecting to MySQL", e)
    finally:
        logger.info("In Finally of DB Connection")
        print("In Finally of DB Connection")
        # if connection.is_connected():
        #     cursor.close()
        #     connection.close()
        #     print("MySQL connection is closed")

def executeDBInsertQuery(connection, statement, data):
    cursor = connection.cursor()
    try:
        result = cursor.execute(statement, data)
        connection.commit()
        logger.info(f"Query executed successfully {statement}")
        return result
    except Error as e:
        logger.info(f"Query execution error '{e}' occurred")

def executeDBExecuteQuery(connection, statement):
    cursor = connection.cursor()
    try:
        cursor.execute(statement)
        logger.info(f"Query executed successfully {statement}")
        return cursor.fetchall()
    except Error as e:
        logger.info(f"Query execution error '{e}' occurred")

def addCandidateDAO(name, address, qualification, jobskill, yearsofexperience):
    print("In Add Candidate DAO Service")
    logger.info("In Add Candidate DAO Service")
    candidateid = random.randint(1,999999)
    logger.info(
        "candidateid " + str(candidateid) + " name " + str(name) + " address " + str(address) + " qualification " + str(qualification) + " jobskill " + str(jobskill) + " yearsofexperience " + str(yearsofexperience))
    print(
        "candidateid " + str(candidateid) + " name " + str(name) + " address " + str(address) + " qualification " + str(qualification) + " jobskill " + str(jobskill) + " yearsofexperience " + str(yearsofexperience))

    insert_stmt = (
        "INSERT INTO candidates (candidateid, name, address, qualification, jobskill, yearsofexperience) "
        "VALUES (%s, %s, %s, %s, %s, %s)"
    )
    data = (candidateid, name, address, qualification, jobskill, yearsofexperience)
    logger.info(insert_stmt, data)
    connection = getMySQLConnection()
    executeDBInsertQuery(connection, insert_stmt, data)

    logger.info("Successfully inserted the candidate entry for the id " + str(jobid))
    return "Successfully inserted the candidate entry for the id " + str(jobid)

def getCandidatesDAO():
    print("In Gets Candidates DB Service")
    logger.info("In Get Candidates DB Service")

    mySql_Get_Candidates_Select_Query = "select * from candidates"
    connection = getMySQLConnection()
    result = executeDBExecuteQuery(connection, mySql_Get_Candidates_Select_Query)
    logger.info("Successfully get the candidates " + str(result))
    return result