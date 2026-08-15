from importlib import reload

import teamwork_implementation_showcase as teamwork_showcase


# Reload the case-study module so local refinements appear on a normal page refresh.
reload(teamwork_showcase)
teamwork_showcase.render_teamwork_implementation_case_study()
