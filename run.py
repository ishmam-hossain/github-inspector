from apps import app
from os import cpu_count


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876, workers=cpu_count(), debug=True)
