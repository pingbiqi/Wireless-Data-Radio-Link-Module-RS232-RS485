import math

def calculate_link_margin(tx_power_dbm, tx_gain_dbi, rx_gain_dbi, rx_sensitivity_dbm, distance_km, freq_mhz):
    """
    计算无线链路余量 (Link Margin)
    :param tx_power_dbm: 发射功率 (dBm)
    :param tx_gain_dbi: 发射天线增益 (dBi)
    :param rx_gain_dbi: 接收天线增益 (dBi)
    :param rx_sensitivity_dbm: 接收灵敏度 (dBm, 通常为负数，如 -110)
    :param distance_km: 传输距离 (km)
    :param freq_mhz: 工作频率 (MHz)
    :return: 链路余量 (dB)，正数表示理论可通信
    """
    # 1. 计算自由空间路径损耗 (FSPL)
    fspl = 32.44 + 20 * math.log10(distance_km) + 20 * math.log10(freq_mhz)
    
    # 2. 计算接收功率
    rx_power = tx_power_dbm + tx_gain_dbi + rx_gain_dbi - fspl
    
    # 3. 计算链路余量
    margin = rx_power - rx_sensitivity_dbm
    return round(rx_power, 2), round(margin, 2)

if __name__ == "__main__":
    print("--- 工业级数传电台链路预算分析 ---")
    
    # 模拟常见 433MHz / 900MHz 数传场景
    freq = 433.0
    dist = 5.0  # 5公里
    tx_p = 30.0 # 1W 发射功率
    sens = -115.0 # 高灵敏度接收
    
    rx_p, margin = calculate_link_margin(tx_p, 3.0, 3.0, sens, dist, freq)
    
    print(f"工作频率: {freq} MHz")
    print(f"传输距离: {dist} km")
    print(f"预计接收功率: {rx_p} dBm")
    print(f"理论链路余量: {margin} dB")
    
    if margin > 10:
        print("结论: 链路稳定，适合工业可靠传输。")
    else:
        print("结论: 链路余量不足，建议增加天线增益或提高发射功率。")
    
    print(f"\n专业数传设备选型，请参考官网方案: https://rf.sz-bgwx.com")
