package com.httpclient.hcq.hc;

import java.io.File;
import java.util.Map;
import java.util.TreeSet;

import com.fhpt.dp.common.util.FileUtil;

public class GenPatch {

	public static void main(String[] args) {
		// File f = new File("e:/price.txt");
		// Map<String, String> numPrices = FileUtil.fieldsPair(f, 0, 1);
		// for (String numId : numPrices.keySet()) {
		// String price = numPrices.get(numId);
		// int price_level;
		// if (price.equals("-1")) {
		// price_level = -1;
		// price = null;
		// } else if (price.equals("0")) {
		// price="免费";
		// price_level = 0;
		// } else {
		// price="￥"+price;
		// price_level = 1;
		// }
		// String sql = "update c_scenicspot set price='" + price + "'
		// ,price_level=" + price_level + " where num_id="
		// + numId + ";";
		// FileUtil.appendRow(new File("e:/price_sql.txt"), sql);
		//// System.out.println(numId + ":" + numPrices.get(numId));
		// }
		// File f1 = new File("e:/baiducity.txt");
		// File f2 = new File("e:/contrycity.txt");
		// Map<String,String> baiducity = FileUtil.fieldsPair(f1, 0, 1);
		// Map<String,String> countrycity = FileUtil.fieldsPair(f2, 0, 1);
		//
		// for(String cityCode :countrycity.keySet()){
		// Boolean flag = false;
		// for(String cityname:baiducity.keySet()){
		// //cityname.contains(countrycity.get(cityCode)
		// if(countrycity.get(cityCode).equals(cityname)){
		// flag = true;
		// String str = cityCode + " " + baiducity.get(cityname);
		// System.out.println(str);
		// }
		// }
		// if(!flag){
		// System.out.println("匹配失败 : " + cityCode + countrycity.get(cityCode));
		// }
		// }
		File baiduFile = new File("e:/baiducity.txt");
		Map<String, String> baiducity = FileUtil.fieldsPair(baiduFile, 1, 0);
		File f = new File("e:/citycode2P.txt");
		Map<String, String> cityCodePinYin = FileUtil.fieldsPair(f, 0, 1, "\\s+");
		String ptn = "insert  into c_city_trip_monitor(city_code,baidu_sname,baidu_surl,create_time,update_time) values ('%s','%s','%s',now(),now());";
		for (String cityCode : cityCodePinYin.keySet()) {
			String pinYin = cityCodePinYin.get(cityCode);
			String name = baiducity.get(pinYin);
			if (name == null) {
				name = "";
			}
			System.out.println(String.format(ptn, cityCode, name, pinYin));
		}

	}
}
