CREATE TABLE IF NOT EXISTS rates
(
	rate_id bigserial   primary key,
	get_date            timestamp,
	rate_base           varchar(5),
	rate_target         varchar(5),
	rate                float
)