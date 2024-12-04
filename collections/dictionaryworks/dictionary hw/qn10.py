product={"Tv":17000,"ac":19000,"washing machine":16000}
discount_price={item: price-(price*10//100) for item,price in product.items()}
print(discount_price)