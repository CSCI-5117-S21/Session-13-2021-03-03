
drop table user_hobby;
drop table user;
drop table hobby;

CREATE TABLE user_data (
    user_id serial primary key,
    username text
);

CREATE TABLE hobby (
    hobby_id serial primary key,
    name text,
    description text,
    created_at timestamp default NOW()
);

CREATE table user_hobby (
    user_id int references user_data,
    hobby_id int references hobby
);

