conct = "postgresql://gorgi:jZ2m-q_ieFujsuFc1trhpQ@free-tier13.aws-eu-central-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dready-pelican-3752"
import psycopg2
mydb = psycopg2.connect(conct)
mycursor = mydb.cursor()

#sql = "DROP TABLE computer_names_table"
#mycursor.execute(sql)
#mycursor.execute("CREATE TABLE computer_names_table (the_number_of_computer "
#                  "VARCHAR(255), computer VARCHAR(255))")
sql = "INSERT INTO circulations_table (the_number_of_circulation, " \
      "circulation) VALUES (%s, %s)"
val = ("1", "א")
mycursor.execute(sql, val)

mydb.commit()
