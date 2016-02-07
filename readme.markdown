# Society of Petroleum Resources Economists

## Installation

    pyenv virtualenv project_name
    pyenv local project_name

Or:
    mkvirtualenv project_name
    workon project_name

Then:

    pip install -r .requirements.base.txt

Sometimes developers may need to `syncdb` without the following apps:

      ...
      'imagestore',
      'imagestore.imagestore_cms',
      'mini_charge',
      'website',
    )

Cover your front end ass(ets):

    python manage.py collectstatic --noinput
