def review(rating):
    assert rating>0,"tooooo low"
    assert rating in range(0,11),"tooo high"
    print("rated")

review(4)