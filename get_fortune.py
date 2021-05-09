#Source: https://colab.research.google.com/github/sarthakmalik/GPT2.Training.Google.Colaboratory/blob/master/Train_a_GPT_2_Text_Generating_Model_w_GPU.ipynb
#Source: https://github.com/minimaxir/gpt-2-simple/blob/master/README.md
import gpt_2_simple as gpt2
import random





def predict():
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='run1')
    s = None
    good = False
    while(good == False):
        good = True
        s = gpt2.generate(sess,
                          length=30,
                          temperature=0.6,  # 0.7
                          prefix="",
                          nsamples=1,
                          batch_size=1,
                          truncate=".",
                          return_as_list=True
                          )[0]
        if(len(s)<4):
            good = False
        if(s.find("\n") != -1):
            good = False


    return s

def main():
    s = predict()

    print(s)






if __name__ == "__main__":
    main()