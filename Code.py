import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# إعداد بيانات افتراضية
np.random.seed(0)  # لتكرار النتائج
students = ['Abdumajeed', 'muaath', 'Anas', 'Ammar', 'Ali']
test1_scores = np.random.randint(50, 100, size=len(students))
test2_scores = np.random.randint(50, 100, size=len(students))

# إنشاء DataFrame
data = {
    'Student': students,
    'Test 1 Score': test1_scores,
    'Test 2 Score': test2_scores
}
df = pd.DataFrame(data)

# عرض البيانات
print("بيانات الطلاب:")
print(df)

# حساب الإحصاءات الأساسية
mean_test1 = np.mean(df['Test 1 Score'])
median_test1 = np.median(df['Test 1 Score'])
std_test1 = np.std(df['Test 1 Score'])

mean_test2 = np.mean(df['Test 2 Score'])
median_test2 = np.median(df['Test 2 Score'])
std_test2 = np.std(df['Test 2 Score'])

# عرض الإحصاءات
print("\nإحصاءات اختبار 1:")
print(f"متوسط الدرجات: {mean_test1:.2f}")
print(f"الوسيط: {median_test1:.2f}")
print(f"الانحراف المعياري: {std_test1:.2f}")

print("\nإحصاءات اختبار 2:")
print(f"متوسط الدرجات: {mean_test2:.2f}")
print(f"الوسيط: {median_test2:.2f}")
print(f"الانحراف المعياري: {std_test2:.2f}")


# إعداد الرسم البياني
plt.figure(figsize=(10, 5))

# رسم الدرجات لاختبار 1
plt.plot(df['Student'], df['Test 1 Score'], marker='o', label='Test 1 Score', color='blue')

# رسم الدرجات لاختبار 2
plt.plot(df['Student'], df['Test 2 Score'], marker='o', label='Test 2 Score', color='green')

# إضافة عنوان وتسميات المحاور
plt.title('students marks in the tests')
plt.xlabel('the students')
plt.ylabel('marks')
plt.legend()

# عرض الرسم البياني
plt.grid(True)
plt.show()



#شرح التنفيذ:
#إنشاء بيانات افتراضية: قمنا بإنشاء بيانات درجات الطلاب باستخدام NumPy وPandas.
#قمنا بتوليد درجات عشوائية لاختبارين للطلاب.
#تحليل البيانات: استخدمنا NumPy لحساب الإحصاءات الأساسية مثل المتوسط و الوسيط والانحراف المعياري لكل اختبار.
#تصور البيانات:استخدمنا Matplotlib لرسم مخطط يوضح درجات الطلاب في الاختبارين.