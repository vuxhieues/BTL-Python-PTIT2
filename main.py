import joblib
import xml.etree.ElementTree as ET
import get_index_permission


def process(filename):
    root = ET.parse(filename).getroot()
    permissions = []
    for item in root.iter("uses-permission"):
        x = item.get("{http://schemas.android.com/apk/res/android}name")
        x = x.split('.')[-1]
        permissions.append(x)
    result = ["Safe", "Not Safe"]
    index_permission = get_index_permission.get_index_permission()

    test_data = [0] * 286

    for i in permissions:
        if i not in index_permission:
            return "Không ổn rồi Đại vương ơi! Cái này em chưa được học!"
        index = index_permission[i]
        test_data[index] = 1

    model = joblib.load("D:\\Code\\BTL\\BTL Python\\Models\\random_forest_model1.joblib")
    return result[model.predict([test_data])[0]]
