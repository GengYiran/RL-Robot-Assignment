import yaml
id_train = [102990, 103095, 103099, 103100, 103104, 103111, 103113, 103271, 103273, 103275, 103276, 103280, 103283, 103292, 103293, 103297, 103299, 103301, 103303, 103305]

# id_test = [100015, 100017, 100021, 100023, 100025]
with open('/home/shengjie/gyr/E2EAff/cfg/push_stapler.yaml', encoding="utf-8") as f:
    content = yaml.safe_load(f)
    # 修改yml文件中的参数
    for (i, id) in enumerate(id_train) :
        print(i, id)
        print(content['env']['asset']['trainObjAssets'])
        content['env']['asset']['trainObjAssets'].update({i: {"name" : id, "path":"dataset/push_stapler_data/{}/mobility.urdf".format(id), 'pointCloud': 'assets/dataset/pap_data/object2pick_2/bag/5/model_normalized_v_pc.npy'}})
        # name: 0
        # path: dataset/pap_data/object2pick_2/bag/5/model_convex_no_wall.urdf
    # for (i, id) in enumerate(id_test) :
    #     print(i, id)
    #     print(content['env']['asset']['testObjAssets'])
    #     content['env']['asset']['testObjAssets'].update({i: {"name" : id, "path":"dataset/open_pot_data/{}/mobility.urdf".format(id)}})
        # name: 0
        # path: dataset/pap_data/object2pick_2/bag/5/model_convex_no_wall.urdf
with open('/home/shengjie/gyr/E2EAff/cfg/new.yaml', 'w', encoding="utf-8") as nf:
    yaml.dump(content, nf)