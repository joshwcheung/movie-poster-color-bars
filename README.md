# Color Bars
Color Bars takes the movie posters of [IMDb's top movies](http://www.imdb.com/chart/top) and performs k-means clustering to produce a color quantized version of each poster. Then, these color quantized posters are used to produce a color bar representing the proportion of each color in the poster.

<section>
    <img width="70" src="color_bars_8/4_the_dark_knight_bar.png" alt="The Dark Knight" hspace="20">
    <img width="70" src="color_bars_8/7_pulp_fiction_bar.png" alt="Pulp Fiction" hspace="20">
    <img width="70" src="color_bars_8/48_apocalypse_now_bar.png" alt="Apocalypse Now" hspace="20">
    <img width="70" src="color_bars_8/61_walle_bar.png" alt="Wall·E" hspace="20">
    <img width="70" src="color_bars_8/75_amelie_bar.png" alt="Amélie" hspace="20">
    <img width="70" src="color_bars_8/198_the_wizard_of_oz_bar.png" alt="The Wizard of Oz" hspace="20">
</section>

# Usage:
	$python color_clustering.py --help
	usage: color_clustering.py [-h] -i IMG -k CLUSTERS
	
	optional arguments:
		-h, --help			show this help message and exit
		-i IMG, --img IMG	Image path
		-k CLUSETERS, --clusters CLUSTERS
							Number of clusters
	
	$python imdb_posters.py --help
	usage: imdb_posters.py [-h] -k CLUSTERS
	
	optional arguments:
		-h, --help			show this help message and exit
		-k CLUSTERS, --clusters CLUSTERS
							Number of clusters
							
# Examples (k = 8): 10/13/15 IMDb Top 10

<section>
    <img width="200" height="300" src="samples/1_the_shawshank_redemption.png" hspace="20">
    <img width="200" height="300" src="samples/1_the_shawshank_redemption_quant.png" hspace="20">
    <img height="300" src="samples/1_the_shawshank_redemption_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/2_the_godfather.png" hspace="20">
    <img width="200" height="300" src="samples/2_the_godfather_quant.png" hspace="20">
    <img height="300" src="samples/2_the_godfather_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/3_the_godfather_part_ii.png" hspace="20">
    <img width="200" height="300" src="samples/3_the_godfather_part_ii_quant.png" hspace="20">
    <img height="300" src="samples/3_the_godfather_part_ii_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/4_the_dark_knight.png" hspace="20">
    <img width="200" height="300" src="samples/4_the_dark_knight_quant.png" hspace="20">
    <img height="300" src="samples/4_the_dark_knight_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/5_12_angry_men.png" hspace="20">
    <img width="200" height="300" src="samples/5_12_angry_men_quant.png" hspace="20">
    <img height="300" src="samples/5_12_angry_men_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/6_schindlers_list.png" hspace="20">
    <img width="200" height="300" src="samples/6_schindlers_list_quant.png" hspace="20">
    <img height="300" src="samples/6_schindlers_list_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/7_pulp_fiction.png" hspace="20">
    <img width="200" height="300" src="samples/7_pulp_fiction_quant.png" hspace="20">
    <img height="300" src="samples/7_pulp_fiction_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/8_the_good_the_bad_and_the_ugly.png" hspace="20">
    <img width="200" height="300" src="samples/8_the_good_the_bad_and_the_ugly_quant.png" hspace="20">
    <img height="300" src="samples/8_the_good_the_bad_and_the_ugly_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/9_the_lord_of_the_rings_the_return_of_the_king.png" hspace="20">
    <img width="200" eight="300" src="samples/9_the_lord_of_the_rings_the_return_of_the_king_quant.png" hspace="20">
    <img height="300" src="samples/9_the_lord_of_the_rings_the_return_of_the_king_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/10_fight_club.png" hspace="20">
    <img width="200" height="300" src="samples/10_fight_club_quant.png" hspace="20">
    <img height="300" src="samples/10_fight_club_bar.png" hspace="20">
</section>

# More Examples (k = 8)

<section>
    <img width="200" height="300" src="samples/14_inception.png" hspace="20">
    <img width="200" height="300" src="samples/14_inception_quant.png" hspace="20">
    <img height="300" src="samples/14_inception_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/16_the_lord_of_the_rings_the_two_towers.png" hspace="20">
    <img width="200" height="300" src="samples/16_the_lord_of_the_rings_the_two_towers_quant.png" hspace="20">
    <img height="300" src="samples/16_the_lord_of_the_rings_the_two_towers_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/82_requiem_for_a_dream.png" hspace="20">
    <img width="200" height="300" src="samples/82_requiem_for_a_dream_quant.png" hspace="20">
    <img height="300" src="samples/82_requiem_for_a_dream_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/130_mad_max_fury_road.png" hspace="20">
    <img width="200" height="300" src="samples/130_mad_max_fury_road_quant.png" hspace="20">
    <img height="300" src="samples/130_mad_max_fury_road_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/169_kill_bill_vol_1.png" hspace="20">
    <img width="200" height="300" src="samples/169_kill_bill_vol_1_quant.png" hspace="20">
    <img height="300" src="samples/169_kill_bill_vol_1_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/68_oldboy.png" hspace="20">
    <img width="200" height="300" src="samples/68_oldboy_quant.png" hspace="20">
    <img height="300" src="samples/68_oldboy_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/61_walle.png" hspace="20">
    <img width="200" height="300" src="samples/61_walle_quant.png" hspace="20">
    <img height="300" src="samples/61_walle_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/53_the_lion_king.png" hspace="20">
    <img width="200" height="300" src="samples/53_the_lion_king_quant.png" hspace="20">
    <img height="300" src="samples/53_the_lion_king_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/31_spirited_away.png" hspace="20">
    <img width="200" height="300" src="samples/31_spirited_away_quant.png" hspace="20">
    <img height="300" src="samples/31_spirited_away_bar.png" hspace="20">
</section>

<section>
    <img width="200" height="300" src="samples/129_my_neighbor_totoro.png" hspace="20">
    <img width="200" height="300" src="samples/129_my_neighbor_totoro_quant.png" hspace="20">
    <img height="300" src="samples/129_my_neighbor_totoro_bar.png" hspace="20">
</section>

To view all 250 color bars, see [color_bars_4](color_bars_4) for k = 4 and [color_bars_8](color_bars_8) for k = 8.
