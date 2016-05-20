# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagesascii', '0002_auto_20160608_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asciiimage',
            name='font',
            field=models.CharField(blank=True, choices=[('0', '1943____'), ('1', '1row'), ('2', '3-d'), ('3', '3d_diagonal'), ('4', '3x5'), ('5', '4max'), ('6', '4x4_offr'), ('7', '5lineoblique'), ('8', '5x7'), ('9', '5x8'), ('10', '64f1____'), ('11', '6x10'), ('12', '6x9'), ('13', 'a_zooloo'), ('14', 'acrobatic'), ('15', 'advenger'), ('16', 'alligator'), ('17', 'alligator2'), ('18', 'alligator3'), ('19', 'alpha'), ('20', 'alphabet'), ('21', 'amc3line'), ('22', 'amc3liv1'), ('23', 'amcaaa01'), ('24', 'amcneko'), ('25', 'amcrazo2'), ('26', 'amcrazor'), ('27', 'amcslash'), ('28', 'amcslder'), ('29', 'amcthin'), ('30', 'amctubes'), ('31', 'amcun1'), ('32', 'aquaplan'), ('33', 'arrows'), ('34', 'asc_____'), ('35', 'ascii___'), ('36', 'ascii_new_roman'), ('37', 'assalt_m'), ('38', 'asslt__m'), ('39', 'atc_____'), ('40', 'atc_gran'), ('41', 'avatar'), ('42', 'B1FF'), ('43', 'b_m__200'), ('44', 'banner'), ('45', 'banner3-D'), ('46', 'banner3'), ('47', 'banner4'), ('48', 'barbwire'), ('49', 'basic'), ('50', 'battle_s'), ('51', 'battlesh'), ('52', 'baz__bil'), ('53', 'bear'), ('54', 'beer_pub'), ('55', 'bell'), ('56', 'benjamin'), ('57', 'big'), ('58', 'bigchief'), ('59', 'bigfig'), ('60', 'binary'), ('61', 'block'), ('62', 'blocks'), ('63', 'bolger'), ('64', 'braced'), ('65', 'bright'), ('66', 'brite'), ('67', 'briteb'), ('68', 'britebi'), ('69', 'britei'), ('70', 'broadway'), ('71', 'broadway_kb'), ('72', 'bubble'), ('73', 'bubble__'), ('74', 'bubble_b'), ('75', 'bulbhead'), ('76', 'c1______'), ('77', 'c2______'), ('78', 'c_ascii_'), ('79', 'c_consen'), ('80', 'calgphy2'), ('81', 'caligraphy'), ('82', 'cards'), ('83', 'catwalk'), ('84', 'caus_in_'), ('85', 'char1___'), ('86', 'char2___'), ('87', 'char3___'), ('88', 'char4___'), ('89', 'charact1'), ('90', 'charact2'), ('91', 'charact3'), ('92', 'charact4'), ('93', 'charact5'), ('94', 'charact6'), ('95', 'characte'), ('96', 'charset_'), ('97', 'chartr'), ('98', 'chartri'), ('99', 'chiseled'), ('100', 'chunky'), ('101', 'clb6x10'), ('102', 'clb8x10'), ('103', 'clb8x8'), ('104', 'cli8x8'), ('105', 'clr4x6'), ('106', 'clr5x10'), ('107', 'clr5x6'), ('108', 'clr5x8'), ('109', 'clr6x10'), ('110', 'clr6x6'), ('111', 'clr6x8'), ('112', 'clr7x10'), ('113', 'clr7x8'), ('114', 'clr8x10'), ('115', 'clr8x8'), ('116', 'coil_cop'), ('117', 'coinstak'), ('118', 'cola'), ('119', 'colossal'), ('120', 'com_sen_'), ('121', 'computer'), ('122', 'contessa'), ('123', 'contrast'), ('124', 'convoy__'), ('125', 'cosmic'), ('126', 'cosmike'), ('127', 'cour'), ('128', 'courb'), ('129', 'courbi'), ('130', 'couri'), ('131', 'crawford'), ('132', 'crazy'), ('133', 'cricket'), ('134', 'cursive'), ('135', 'cyberlarge'), ('136', 'cybermedium'), ('137', 'cybersmall'), ('138', 'cygnet'), ('139', 'd_dragon'), ('140', 'DANC4'), ('141', 'dancingfont'), ('142', 'dcs_bfmo'), ('143', 'decimal'), ('144', 'deep_str'), ('145', 'defleppard'), ('146', 'demo_1__'), ('147', 'demo_2__'), ('148', 'demo_m__'), ('149', 'devilish'), ('150', 'diamond'), ('151', 'dietcola'), ('152', 'digital'), ('153', 'doh'), ('154', 'doom'), ('155', 'dosrebel'), ('156', 'dotmatrix'), ('157', 'double'), ('158', 'doubleshorts'), ('159', 'drpepper'), ('160', 'druid___'), ('161', 'dwhistled'), ('162', 'e__fist_'), ('163', 'ebbs_1__'), ('164', 'ebbs_2__'), ('165', 'eca_____'), ('166', 'eftichess'), ('167', 'eftifont'), ('168', 'eftipiti'), ('169', 'eftirobot'), ('170', 'eftitalic'), ('171', 'eftiwall'), ('172', 'eftiwater'), ('173', 'epic'), ('174', 'etcrvs__'), ('175', 'f15_____'), ('176', 'faces_of'), ('177', 'fair_mea'), ('178', 'fairligh'), ('179', 'fantasy_'), ('180', 'fbr12___'), ('181', 'fbr1____'), ('182', 'fbr2____'), ('183', 'fbr_stri'), ('184', 'fbr_tilt'), ('185', 'fender'), ('186', 'filter'), ('187', 'finalass'), ('188', 'fire_font-k'), ('189', 'fire_font-s'), ('190', 'fireing_'), ('191', 'flipped'), ('192', 'flowerpower'), ('193', 'flyn_sh'), ('194', 'fourtops'), ('195', 'fp1_____'), ('196', 'fp2_____'), ('197', 'fraktur'), ('198', 'funface'), ('199', 'funfaces'), ('200', 'funky_dr'), ('201', 'future_1'), ('202', 'future_2'), ('203', 'future_3'), ('204', 'future_4'), ('205', 'future_5'), ('206', 'future_6'), ('207', 'future_7'), ('208', 'future_8'), ('209', 'fuzzy'), ('210', 'gauntlet'), ('211', 'georgi16'), ('212', 'georgia11'), ('213', 'ghost'), ('214', 'ghost_bo'), ('215', 'ghoulish'), ('216', 'glenyn'), ('217', 'goofy'), ('218', 'gothic'), ('219', 'gothic__'), ('220', 'graceful'), ('221', 'gradient'), ('222', 'graffiti'), ('223', 'grand_pr'), ('224', 'greek'), ('225', 'green_be'), ('226', 'hades___'), ('227', 'heart_left'), ('228', 'heart_right'), ('229', 'heavy_me'), ('230', 'helv'), ('231', 'helvb'), ('232', 'helvbi'), ('233', 'helvi'), ('234', 'henry3d'), ('235', 'heroboti'), ('236', 'hex'), ('237', 'hieroglyphs'), ('238', 'high_noo'), ('239', 'hills___'), ('240', 'hollywood'), ('241', 'home_pak'), ('242', 'horizontalleft'), ('243', 'horizontalright'), ('244', 'house_of'), ('245', 'hypa_bal'), ('246', 'hyper___'), ('247', 'ICL-1900'), ('248', 'impossible'), ('249', 'inc_raw_'), ('250', 'invita'), ('251', 'isometric1'), ('252', 'isometric2'), ('253', 'isometric3'), ('254', 'isometric4'), ('255', 'italic'), ('256', 'italics_'), ('257', 'ivrit'), ('258', 'jacky'), ('259', 'jazmine'), ('260', 'jerusalem'), ('261', 'joust___'), ('262', 'katakana'), ('263', 'kban'), ('264', 'keyboard'), ('265', 'kgames_i'), ('266', 'kik_star'), ('267', 'knob'), ('268', 'konto'), ('269', 'kontoslant'), ('270', 'krak_out'), ('271', 'larry3d'), ('272', 'lazy_jon'), ('273', 'lcd'), ('274', 'lean'), ('275', 'letter_w'), ('276', 'letters'), ('277', 'letterw3'), ('278', 'lexible_'), ('279', 'lildevil'), ('280', 'lineblocks'), ('281', 'linux'), ('282', 'lockergnome'), ('283', 'mad_nurs'), ('284', 'madrid'), ('285', 'magic_ma'), ('286', 'marquee'), ('287', 'master_o'), ('288', 'maxfour'), ('289', 'mayhem_d'), ('290', 'mcg_____'), ('291', 'merlin1'), ('292', 'merlin2'), ('293', 'mig_ally'), ('294', 'mike'), ('295', 'mini'), ('296', 'mirror'), ('297', 'mnemonic'), ('298', 'modern__'), ('299', 'modular'), ('300', 'morse'), ('301', 'morse2'), ('302', 'moscow'), ('303', 'mshebrew210'), ('304', 'muzzle'), ('305', 'nancyj-fancy'), ('306', 'nancyj-improved'), ('307', 'nancyj-underlined'), ('308', 'nancyj'), ('309', 'new_asci'), ('310', 'nfi1____'), ('311', 'nipples'), ('312', 'notie_ca'), ('313', 'npn_____'), ('314', 'nscript'), ('315', 'ntgreek'), ('316', 'nvscript'), ('317', 'o8'), ('318', 'octal'), ('319', 'odel_lak'), ('320', 'ogre'), ('321', 'ok_beer_'), ('322', 'oldbanner'), ('323', 'os2'), ('324', 'outrun__'), ('325', 'p_s_h_m_'), ('326', 'p_skateb'), ('327', 'pacos_pe'), ('328', 'panther_'), ('329', 'pawn_ins'), ('330', 'pawp'), ('331', 'peaks'), ('332', 'peaksslant'), ('333', 'pebbles'), ('334', 'pepper'), ('335', 'phonix__'), ('336', 'platoon2'), ('337', 'platoon_'), ('338', 'pod_____'), ('339', 'poison'), ('340', 'puffy'), ('341', 'puzzle'), ('342', 'pyramid'), ('343', 'r2-d2___'), ('344', 'rad_____'), ('345', 'rad_phan'), ('346', 'radical_'), ('347', 'rainbow_'), ('348', 'rally_s2'), ('349', 'rally_sp'), ('350', 'rammstein'), ('351', 'rampage_'), ('352', 'rastan__'), ('353', 'raw_recu'), ('354', 'rci_____'), ('355', 'rectangles'), ('356', 'red_phoenix'), ('357', 'relief'), ('358', 'relief2'), ('359', 'rev'), ('360', 'reverse'), ('361', 'ripper!_'), ('362', 'road_rai'), ('363', 'rockbox_'), ('364', 'rok_____'), ('365', 'roman'), ('366', 'roman___'), ('367', 'rot13'), ('368', 'rotated'), ('369', 'rounded'), ('370', 'rowancap'), ('371', 'rozzo'), ('372', 'runic'), ('373', 'runyc'), ('374', 's-relief'), ('375', 'sans'), ('376', 'sansb'), ('377', 'sansbi'), ('378', 'sansi'), ('379', 'santaclara'), ('380', 'sblood'), ('381', 'sbook'), ('382', 'sbookb'), ('383', 'sbookbi'), ('384', 'sbooki'), ('385', 'script'), ('386', 'script__'), ('387', 'serifcap'), ('388', 'shadow'), ('389', 'shimrod'), ('390', 'short'), ('391', 'skate_ro'), ('392', 'skateord'), ('393', 'skateroc'), ('394', 'sketch_s'), ('395', 'slant'), ('396', 'slide'), ('397', 'slscript'), ('398', 'sm______'), ('399', 'small'), ('400', 'smallcaps'), ('401', 'smisome1'), ('402', 'smkeyboard'), ('403', 'smpoison'), ('404', 'smscript'), ('405', 'smshadow'), ('406', 'smslant'), ('407', 'smtengwar'), ('408', 'soft'), ('409', 'space_op'), ('410', 'spc_demo'), ('411', 'speed'), ('412', 'spliff'), ('413', 'stacey'), ('414', 'stampate'), ('415', 'stampatello'), ('416', 'standard'), ('417', 'star_war'), ('418', 'starstrips'), ('419', 'starwars'), ('420', 'stealth_'), ('421', 'stellar'), ('422', 'stencil1'), ('423', 'stencil2'), ('424', 'stforek'), ('425', 'stop'), ('426', 'straight'), ('427', 'street_s'), ('428', 'sub-zero'), ('429', 'subteran'), ('430', 'super_te'), ('431', 'swampland'), ('432', 'swan'), ('433', 'sweet'), ('434', 't__of_ap'), ('435', 'tanja'), ('436', 'tav1____'), ('437', 'taxi____'), ('438', 'tec1____'), ('439', 'tec_7000'), ('440', 'tecrvs__'), ('441', 'tengwar'), ('442', 'term'), ('443', 'test1'), ('444', 'thick'), ('445', 'thin'), ('446', 'threepoint'), ('447', 'ti_pan__'), ('448', 'ticks'), ('449', 'ticksslant'), ('450', 'tiles'), ('451', 'times'), ('452', 'timesofl'), ('453', 'tinker-toy'), ('454', 'tomahawk'), ('455', 'tombstone'), ('456', 'top_duck'), ('457', 'train'), ('458', 'trashman'), ('459', 'trek'), ('460', 'triad_st'), ('461', 'ts1_____'), ('462', 'tsalagi'), ('463', 'tsm_____'), ('464', 'tsn_base'), ('465', 'tty'), ('466', 'ttyb'), ('467', 'tubular'), ('468', 'twin_cob'), ('469', 'twisted'), ('470', 'twopoint'), ('471', 'type_set'), ('472', 'ucf_fan_'), ('473', 'ugalympi'), ('474', 'unarmed_'), ('475', 'univers'), ('476', 'usa_____'), ('477', 'usa_pq__'), ('478', 'usaflag'), ('479', 'utopia'), ('480', 'utopiab'), ('481', 'utopiabi'), ('482', 'utopiai'), ('483', 'varsity'), ('484', 'vortron_'), ('485', 'war_of_w'), ('486', 'wavy'), ('487', 'weird'), ('488', 'wetletter'), ('489', 'whimsy'), ('490', 'wow'), ('491', 'xbrite'), ('492', 'xbriteb'), ('493', 'xbritebi'), ('494', 'xbritei'), ('495', 'xchartr'), ('496', 'xchartri'), ('497', 'xcour'), ('498', 'xcourb'), ('499', 'xcourbi'), ('500', 'xcouri'), ('501', 'xhelv'), ('502', 'xhelvb'), ('503', 'xhelvbi'), ('504', 'xhelvi'), ('505', 'xsans'), ('506', 'xsansb'), ('507', 'xsansbi'), ('508', 'xsansi'), ('509', 'xsbook'), ('510', 'xsbookb'), ('511', 'xsbookbi'), ('512', 'xsbooki'), ('513', 'xtimes'), ('514', 'xtty'), ('515', 'xttyb'), ('516', 'yie-ar__'), ('517', 'yie_ar_k'), ('518', 'z-pilot_'), ('519', 'zig_zag_'), ('520', 'zone7___')], max_length=128, null=True),
        ),
    ]
