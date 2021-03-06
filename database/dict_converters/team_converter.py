from database.dict_converters.converter_base import ConverterBase


class TeamConverter(ConverterBase):
    SUBVERSIONS = {  # Increment every time a change to the dict is made
        3: 0,
    }

    @classmethod
    def convert(cls, teams, dict_version):
        CONVERTERS = {
            3: cls.teamsConverter_v3,
        }
        converted_teams = CONVERTERS[dict_version](cls._listify(teams))
        return cls._delistify(converted_teams)

    @classmethod
    def teamsConverter_v3(cls, teams):
        return map(cls.teamConverter_v3, teams)

    @classmethod
    def teamConverter_v3(cls, team):
        has_nl = team.nl and team.nl.city and team.nl.state_prov and team.nl.country
        team_dict = {
            'key': team.key.id(),
            'team_number': team.team_number,
            'nickname': team.nickname,
            'name': team.name,
            'website': team.website,
            'rookie_year': team.rookie_year,
            'motto': team.motto,
            'home_championship': team.championship_location,
        }
        team_dict.update(cls.constructLocation_v3(team))
        return team_dict
