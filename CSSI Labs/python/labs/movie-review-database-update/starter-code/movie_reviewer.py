#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

inside_movie = {
    "title": "Inside Out",
    "id": "tt2096673",
    "year_released": 2012,
    "rating": "PG",
    "score": 7.5,
    "out_of": 10,
    "reviews": 463787
}

# Do not edit the code above!

# Write your code below to update the information in accordance with its
# IMDB page: http://www.imdb.com/title/tt2096673/



#part 1
inside_movie["year_released"] = 2015
inside_movie["score"] = 8.2
inside_movie[ "reviews"] = 885
inside_movie.pop( "out_of")
inside_movie["genre"] = ["Animation", "Adventure", "Comedy", "Family", "Drama", "Fantasty"]


print( inside_movie )

class movies( object ):
    def __init__( self, title, id, year, rating, score, reviews ):
        self.title = title
        self.id = id
        self.year = year
        self.rating = rating
        self.score = score

# part 2
inside_out = movies( "Inside Out", "tt2096673", 2015, "PG", 7.5, 885 )
princess_bride = movies( "The Princess Bride", "tt0093779", 1987, "PG", 8.1, 760 )
black_panther = movies( "Black Panther", "tt1825683", 2018, "PG-13", 7.5, 2224 )

#part 3
movies = [inside_out, princess_bride, black_panther]
