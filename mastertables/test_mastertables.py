#!./env/bin/python

import mastertables

# TEAM_ = "HEGCWYCGRRQEYPZYMBZBJUOOQQTNUW"
TEAM_ = "JZMWPTDRYIXWATTHLBAALQNDMXTMRA"
# VOC_ = "407099de-17dd-4fe1-a7cc-d38e46a0ab95"
VOC_ = "7dbd2fdf-fbc9-45ef-ac8b-0e58c183f0e9"
# HOST_ = "http://localhost:8001/"
HOST_ = "https://mastertables.athento.com/"

def main():
    mt = mastertables.MasterTablesClient(TEAM_, host=HOST_)
    print("")
    print("get_vocabulary")
    print(mt.get_vocabulary(VOC_))
    print("")
    print("======================================================================")
    print("")
    print("get_vocabulary_reverse")
    print(mt.get_vocabulary_reverse(VOC_))
    print("")
    print("======================================================================")
    print("")
    print("get_values")
    print(mt.get_values(VOC_))
    print("")

if __name__ == '__main__':
    main()
