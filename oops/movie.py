class Movie:
    title:str
    rating:int
    run_time:int
    director:str
    genre:str

    def set_movie(self,title,rating,run_time,director,genre):
      self.title=title
      self.rating=rating
      self.run_time=run_time
      self.director=director
      self.genre=genre
    def display_movie(self):
       print(self.title,self.rating,self.run_time,self.director,self.genre)

movie_instance1=Movie()
movie_instance1.set_movie("arm",4.4,120,"jithin lal","action")

movie_instance1.display_movie()