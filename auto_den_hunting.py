from communal import *

print(f'Delay for {args.delay} seconds.')
print(f'开始自动开车任务！')
sleep(args.delay)

try:
    raid_counter = 1
    while raid_counter >= 0:
        print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 第 {raid_counter} 车开始...')
        # 战斗准备
        battle_preparation()
        print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 招募开始 等待: {args.recruit_duration}s')
        recruiting_players(args.recruit_duration)
        battle = args.battle_duration if args.exit_mode == 'flight' else 30
        print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 开始战斗 等待: {battle}s')
        start_raid = time.time()
        while time.time() - start_raid < battle:
            remaining = battle - (time.time() - start_raid)
            send(ns_A)
            sleep(0.5)
        way = '重启游戏' if args.exit_mode == 'flight' else '飞行模式'
        print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 退出战斗 退出方式: {way}')
        exit_raid(args.exit_mode)
        raid_counter += 1

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
