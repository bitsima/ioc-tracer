from sqlalchemy import orm

from ..models import yara_rule_model
from ..api import schemas


async def create_rule(rule: schemas.YaraRule, session: orm.Session) -> schemas.YaraRule:
    rule = yara_rule_model.YaraRule(**rule.model_dump())
    session.add(rule)
    session.commit()
    session.refresh(rule)

    return schemas.YaraRule(**rule.__dict__)


async def get_rules(session: orm.Session, fetch_size=-1) -> list[schemas.YaraRule]:
    if fetch_size == -1:
        rules = session.query(yara_rule_model.YaraRule).all()
    else:
        rules = session.query(yara_rule_model.YaraRule).limit(fetch_size).all()

    return list(map(schemas.YaraRule.model_validate, rules))


async def get_rule(rule_name: str, session: orm.Session) -> yara_rule_model.YaraRule:
    rule = (
        session.query(yara_rule_model.YaraRule)
        .filter(yara_rule_model.YaraRule.rule_name == rule_name)
        .first()
    )
    return rule


async def delete_rule(
    yara_rule: yara_rule_model.YaraRule, session: orm.Session
) -> None:
    session.delete(yara_rule)
    session.commit()
