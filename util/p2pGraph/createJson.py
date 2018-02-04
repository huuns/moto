# -*- coding: utf-8 -*-


import simplejson as json

p2p_company_list = [ '금요일펀딩','넥스트펀딩','더좋은펀드','줌펀드','랑펀드','래더펀딩','렌딧','렌딩사이언스','론포인트','루프펀딩','모아펀딩','모우다','미드레이트','바로펀딩','바른펀드','펀펀딩','브릿지펀딩','BF365','비욘드펀드','비플러스','빅파이펀딩','빌드온펀딩','빌리','소딧','스마트크라우드','스마트펀딩','시소펀딩','썬펀딩','어니스트 펀드','어메이징펀드','8퍼센트','엘리펀드','올리펀딩','위펀딩','유니어스펀딩','유엔아이펀딩','이디움펀딩','이지펀딩','제트크라우드','코리아펀딩','코인럭','펀딩플랫폼','탱커펀드','테라펀딩','투게더앱스','칵테일펀딩','팝펀딩','펀다','펀듀','펀디드','펀한펀딩','포켓펀딩','프로핏','피플펀드','핀스트리트','헬로펀딩']


p2p_total_output = [2067100000,1247500000,1059000000,4615500000,1000000000,2070000000,52232547304,2870000000,3182000000,114250000000,20356230000,4508520000,2204450000,2685920000,2760000000,12256100000,745000000,6176000000,19573300000,504500000,3232528221,1570000000,75211260000,37995700000,1620600000,4720000000,22998100000,30000000,29386500000,260000000,76073450000,6166400000,9396830000,3789849237,4183000000,80000000,25576400000,720000000,7152600000,61191330000,0,38379800000,16408500000,147513000000,67951500000,800000000,56028653000,19350619848,61774750000,6834700000,0,380000000,7939000000,78291100000,8430510000,25200000000]


p2p_remain_output = [1467100000,1247500000,725500000,3594387207,1000000000,2070000000,33288074432,2250000000,1382000000,76950000000,14940000000,3168526505,1601490606,800000000,1830000000,3798900000,621680412,1838879221,16942000000,348364257,2751000000,1570000000,35818316299,12563000000,559832971,3200000000,8722500000,30000000,18861869888,200000000,35132683741,4654200000,1443562557,2999849237,3406500000,80000000,16300000000,670000000,6731600000,20976200000,0,25012200000,7052972963,71275000000,28879500000,400000000,28452275214,8207895571,23780000000,5440675000,0,380000000,5710861909,40461890813,2287310000,16900000000]



tcJSON = {}

jsonFile = './p2p_info_201706.json'
with open (jsonFile, 'w') as f:

    for idx, cname in enumerate(p2p_company_list):

        tcJSON[cname] = {}

        tcJSON[cname]['누적대출액'] = p2p_total_output[idx]
        tcJSON[cname]['대출잔액'] = p2p_remain_output[idx]

        # targetDayList = []
        # for td in range(13, -1, -1):
        #     targetDay = date.today() - timedelta(td)
        #     targetDayList.append(targetDay)
        # print targetDayList
        #
        # for eid, each_date in enumerate(targetDayList):
        #     eachObj = TrackingChannel.objects.filter(category_name=category_name, today=each_date)
        #
        #     if len(eachObj) == 0:
        #         continue
        #     else:
        #         tcJSON[category_name.encode('utf-8')][str(each_date)] = {}
        #         for idx, each in enumerate(eachObj):
        #             tcJSON[category_name.encode('utf-8')][str(each_date)][str(idx)] = {
        #                     'channel_title'    : each.channel_title.encode('utf-8'),
        #                     'channel_type'     : each.channel_type,
        #                     'channel_id'       : each.channel_id,
        #                     'view_count'       : each.view_count,
        #                     'comment_count'    : each.comment_count,
        #                     'subscriber_count' : each.subscriber_count,
        #                     'video_count'      : each.video_count,
        #                     'channel_thumbnail': each.channel_thumbnail
        #             }

    jsonString = json.dumps(tcJSON, sort_keys=True, indent=4 * ' ')
    f.write(jsonString)
