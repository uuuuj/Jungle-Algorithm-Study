def solution(bandage, health, attacks):
    cur_health = health
    attack_idx = 0
    bandage_count = 0
    attack_time, damage = attacks[attack_idx]
    act_time, hps, bouns = bandage
    
    for i in range(1, attacks[-1][0] + 1):
        
        # 공격 받을때
        if attack_time == i:
            cur_health -= damage
            bandage_count = 0
            
            if cur_health <= 0:
                cur_health = -1
                break
            
            if attack_idx < len(attacks) - 1:
                attack_idx += 1
                attack_time, damage = attacks[attack_idx]
        
        # 받지 않을때
        else:
            if cur_health < health:
                cur_health += hps
                bandage_count += 1
                
                if bandage_count == act_time:
                    cur_health += bouns
                    bandage_count = 0
                
                cur_health = health if cur_health >= health else cur_health
        
    return cur_health