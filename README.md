# MembersAPI
REST APIs for accessing Members info


CSV Upload: Only unique Client_member_id and Phone number records will be uploaded. Duplicates are ignored by check uniquenes )


To create Sqlite Database, run bash script $./run_migrations.sh


# URLs:

GET ^members/ ==> for all members

GET ^members/?column_name=value ==> Search by columns names

POST ^members/ ==> Create new members

POST ^upload_csv/$ ==> Upload a Binary data





