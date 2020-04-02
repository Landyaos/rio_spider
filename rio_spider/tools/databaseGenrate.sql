create table if not exists comment
(
    id       bigint auto_increment
        primary key,
    content  text         null,
    date     date         null,
    movie_id varchar(255) null,
    rate     float        null,
    user_id  varchar(255) null,
    votes    bigint       null
);

create table if not exists director_screenwriter
(
    id              bigint auto_increment
        primary key,
    cover_url       varchar(255) null,
    foreign_name    varchar(255) null,
    is_director     bit          null,
    is_screenwriter bit          null,
    name            varchar(255) null,
    url_douban      varchar(255) null,
    url_imdb        varchar(255) null,
    photos          varchar(511) null,
    awards          varchar(511) null,
    profile         text         null
);

create table if not exists genre
(
    id           bigint auto_increment
        primary key,
    description  varchar(255) null,
    foreign_name varchar(255) null,
    name         varchar(255) not null
);

create table if not exists movie
(
    id           bigint auto_increment
        primary key,
    name         varchar(255) not null,
    foreign_name varchar(255) null,
    length       bigint       null,
    language     varchar(255) null,
    area         varchar(255) null,
    release_date date         null,
    cover_url    varchar(255) null,
    rate         float        null,
    rate_num     bigint       null,
    weight       varchar(255) null,
    url_douban   varchar(255) null,
    id_douban    varchar(255) null,
    url_imdb     varchar(255) null,
    profile      text         null,
    trailer      varchar(511) null
);

create table if not exists movie_director_relation
(
    id       bigint auto_increment
        primary key,
    director varchar(255) null,
    ranking  int          null,
    movie_id varchar(255) null,
    url      varchar(100) null
);

create table if not exists movie_genre_relation
(
    id       bigint auto_increment
        primary key,
    genre    varchar(255) null,
    movie_id varchar(255) null
);

create table if not exists movie_screenwriter_relation
(
    id           bigint auto_increment
        primary key,
    ranking      int          null,
    movie_id     varchar(255) null,
    screenwriter varchar(255) null,
    url          varchar(100) null
);

create table if not exists movie_starring_relation
(
    id       bigint auto_increment
        primary key,
    movie_id varchar(255) null,
    starring varchar(255) null,
    ranking  int          null,
    url      varchar(100) null
);

create table if not exists review
(
    id       bigint auto_increment
        primary key,
    content  text         null,
    date     date         null,
    movie_id varchar(255) null,
    rate     float        null,
    title    varchar(255) null,
    user_id  varchar(255) null,
    votes    bigint       null
);

create table if not exists starring
(
    id           bigint auto_increment
        primary key,
    cover_url    varchar(255) null,
    foreign_name varchar(255) null,
    name         varchar(255) null,
    url_douban   varchar(255) null,
    url_imdb     varchar(255) null,
    profile      text         null,
    photos       varchar(511) null,
    awards       varchar(511) null
);

create table if not exists user
(
    id        bigint auto_increment
        primary key,
    icon      varchar(255) null,
    id_douban varchar(255) null,
    url       varchar(255) null,
    username  varchar(255) not null
);

