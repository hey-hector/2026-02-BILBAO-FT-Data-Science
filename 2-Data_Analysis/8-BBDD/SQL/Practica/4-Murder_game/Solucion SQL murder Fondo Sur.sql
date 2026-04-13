SELECT date,type,description,city
FROM crime_scene_report
WHERE city == "SQL City" and type == "murder" and date = "20180115";

SELECT *
FROM interview
JOIN person on person.id WHERE person.id == interview.person_id and address_street_name in ("Franklin Ave") and person.name like "Annabel%";

SELECT person.name, interview.transcript
FROM interview
JOIN person on person.id 
WHERE person.id == interview.person_id and address_street_name in ("Northwestern Dr")
and person.address_number = (select max(address_number) from person where address_street_name = 'Northwestern Dr');

select max(address_number) from person where address_street_name = 'Northwestern Dr';

SELECT *
FROM get_fit_now_member
WHERE membership_status like "%Gold%" and get_fit_now_member.id like "48Z%";

SELECT *
FROM person
JOIN drivers_license on person.license_id = drivers_license.id
WHERE person.id in (28819, 67318); -- Jeremy Bowers es el asesino!

SELECT *
FROM person
JOIN get_fit_now_member on person.id = get_fit_now_member.person_id
JOIN get_fit_now_check_in on get_fit_now_check_in.membership_id = get_fit_now_member.id
WHERE person.name in ("Joe Germuska", "Jeremy Bowers"); -- Coinciden los dos sospechosos en el mismo check-in por lo que no es relevante

SELECT *
FROM facebook_event_checkin
WHERE person_id in(28819,67318,16371);

SELECT *
FROM interview
WHERE person_id == 67318;

SELECT *
FROM person p
JOIN facebook_event_checkin f on p.id = f.person_id
JOIN drivers_license d on p.license_id = d.id
WHERE d.hair_color == "red" and gender == "female" and car_make == "Tesla" and (height between 65 and 67); -- Miranda es la cabecilla

SELECT *
FROM interview
WHERE person_id == 99716;

