from classifier import Classifier

def main():
    data_dir = "training/"
    test_dir = "testing/"
    c = Classifier(data_dir,test_dir, "hipo")
    c.net_training()
    c.save("hipo")
    c.load("hipo")
    print("not hipos")
    c.predict("training/zebras/google-image(0004).jpeg")
    c.predict("training/zebras/google-image(0006).jpeg")
    c.predict("training/zebras/google-image(0007).jpeg")
    c.predict("training/zebras/google-image(0009).jpeg")
    c.predict("training/zebras/google-image(0002).jpeg")
    c.predict("training/zebras/google-image(0003).jpeg")
    c.predict("training/zebras/google-image(0017).jpeg")
    print("hipos")
    c.predict("testing/Choeropsis_liberiensis/google-image(0002).jpeg")
    c.predict("testing/Choeropsis_liberiensis/google-image(0003).jpeg")
    c.predict("testing/Choeropsis_liberiensis/google-image(0005).jpeg")
    c.predict("testing/Choeropsis_liberiensis/google-image(0006).jpeg")
    c.predict("testing/Choeropsis_liberiensis/google-image(0008).jpeg")
    c.predict("testing/Choeropsis_liberiensis/google-image(0007).jpeg")

if __name__ == '__main__':
    main()
