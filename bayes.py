from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

def Load_data(data_dir):
    return open(data_dir, "r", encoding = "utf-8").readlines()

class Crowded():
    def __init__(self, data_full, data_nfull):
        self.vectorizer = CountVectorizer()
        self.nb_classifier = MultinomialNB()

        # load các data
        self.data_full = Load_data(data_full)
        self.data_nfull = Load_data(data_nfull)

        # Tạo tập huấn luyện và tập kiểm tra bằng phương pháp train_test_split
        X = self.data_full + self.data_nfull
        y = [1] * len(self.data_full) + [0] * len(self.data_nfull)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # chuyển đổi văn bản thành vector đặc trưng rồi huấn luyện mô hình
    def training(self):
        self.X_train = self.vectorizer.fit_transform(self.X_train)
        self.X_test = self.vectorizer.transform(self.X_test)
        self.nb_classifier.fit(self.X_train, self.y_train)

    # xác định ảnh mới là đông hay không đông
    def filterr(self, new_image_vector):
        self.training()
        X_new = self.vectorizer.transform([new_image_vector])
        filterr = self.nb_classifier.predict(X_new)

        if filterr[0]: return "Kẹt xe."
        else: return "Không kẹt xe."