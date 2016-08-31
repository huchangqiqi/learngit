package t1;

import java.io.File;
import java.io.FileWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
import java.sql.PreparedStatement;
import java.sql.ResultSet;


public class Tmysql {

	private Connection conn = null;
	PreparedStatement statement = null;
	
	//conncet
	void connSQL(){
		String url = "jdbc:mysql://10.95.132.8:3306/type_fix?characterEncoding=UTF-8";
		String username = "root";
		String password = "123456";
		
		try{
			Class.forName("com.mysql.jdbc.Driver");
			conn = DriverManager.getConnection(url,username,password);
			
		}catch (ClassNotFoundException cnfex) {
			System.err.println("jbbc failed");
			cnfex.printStackTrace();
		}catch (SQLException sqlex){
			System.err.println("failed to mysql");
			sqlex.printStackTrace();
		}
	}
	
	void deconnSQL(){
		try {
			if(conn != null){
				conn.close();
			}
		}catch (Exception e){
			System.out.println("disconn to mysql");
			e.printStackTrace();
		}
	}
	
	ResultSet selectSQL(String sql){
		ResultSet rs = null;
		try{
			statement = conn.prepareStatement(sql);
			rs = statement.executeQuery(sql);
		}catch (SQLException e){
			e.printStackTrace();
		}
		
		return rs;
		
	}
	boolean insertSQL(String sql){
		try {
			statement = conn.prepareStatement(sql);
			statement.executeUpdate();
			return true;
		}catch (SQLException e){
			System.out.println("插入数据库时出错：");
			e.printStackTrace();
		}catch (Exception e){
			System.out.println("插入时出错");
			e.printStackTrace();
		}
		return false;
	}
	
	void show1(ResultSet rs1,ResultSet rs2 ,ResultSet rs3){
		Set<Long> scenicNumIds=loadScenicNumIds();
		try{
			
			Set<String> ccstTypeSet  = new HashSet<>();
			
			
			
            //携程到平台景点类型对应map
			Map<String,Set<Long>> ctripTypeMap = new HashMap<>();
			while(rs1.next()){
				String type=rs1.getString("ccst_type");
				ccstTypeSet.add(type);
				long cstId=rs1.getLong("cst_id");
				Set<Long> ts = ctripTypeMap.get(type);
				if( ts == null){
					ts = new HashSet<Long>();
					ctripTypeMap.put(type, ts);
				}
				ts.add(cstId);
			}
			
			Set<String> tsiTypeSet = new HashSet<>();
			Map<Long,Set<Long>> allScenicPlatformTypes = new HashMap<>();
			while(rs2.next()){
				long numId=rs2.getLong("tsi_tn_id");
				if(!scenicNumIds.contains(numId)){
					continue;
				}
				String ctripType=rs2.getString("tsi_type");
				
				String[] types = ctripType==null?new String[0]:ctripType.split("\\s+");
				
				
				Set<Long> scenicPlatformTypes=new HashSet<>();
				for(String type:types){
					Set<Long> platformTypes=ctripTypeMap.get(type);
					if(platformTypes!=null){
						scenicPlatformTypes.addAll(platformTypes);
					}
					tsiTypeSet.add(type);
				}
				//System.out.println(numId+":"+scenicPlatformTypes);
				if(!scenicPlatformTypes.isEmpty()){
					allScenicPlatformTypes.put(numId, scenicPlatformTypes);					
				}

			}
			
			
			
			
			Map<Long,Set<Long>> cScenicTypes = new HashMap<>();
			while(rs3.next()){
				long numId = rs3.getLong("num_id");
				long cstId = rs3.getLong("cst_id");
				
				Set<Long> ms = cScenicTypes.get(numId);
				if(ms == null){
					ms = new HashSet<Long>();
					cScenicTypes.put(numId, ms);
				}
				ms.add(cstId);
			}
			
			FileWriter w = new FileWriter("c:"+File.separator+"res.txt");
			
			int i = 0;
			Iterator<Long> iter = scenicNumIds.iterator();
			while(iter.hasNext()){
				long numKey = iter.next();
				Set<Long> cST = cScenicTypes.get(numKey);
				Set<Long> aSPT = allScenicPlatformTypes.get(numKey);
				
				if( !isSetEqual(cST,aSPT)){
					
					i++;
					System.out.println(numKey+":" + cST + " " + aSPT );
					
					w.write(numKey+":"+ cST + " " + aSPT + "\r\n");
					
				}
			}
			System.out.println("sum error = " + i);
			
			
			Iterator iteccTS = ccstTypeSet.iterator();
			Iterator itetTS = tsiTypeSet.iterator();
			while(iteccTS.hasNext()){
				String tmp = (String) iteccTS.next();
				if(!tsiTypeSet.contains(tmp)){
					System.out.println(tmp + " ");
				}
			}
			
			if(isSetEqual(ccstTypeSet,tsiTypeSet )){
				System.out.println("equal!!!");
			}
			
			
			System.out.println("size of ccstTypeSet : " + ccstTypeSet.size() +"\r\n" + "size of tsiTypeSet: " + tsiTypeSet.size());
			
			
			
			
			System.out.println();
			//w.write("sum error = " + i + "\r\n");
			w.close();
			
			
		}catch (SQLException e)
		{
			e.printStackTrace();
		}catch (Exception e){
			e.printStackTrace();
		}
		
	}
	public static boolean isSetEqual(Set set1,Set set2){
		if(set1 == null && set2 == null){
			return true;
		}
		if(set1 == null || set2 == null || set1.size() !=  set2.size() 
				|| set1.size() == 0 || set2.size() == 0){
			return false;
		}
		
		//Iterator ite1 = set1.iterator();
		Iterator ite2 = set2.iterator();
		boolean isEqual = true;
		while(ite2.hasNext()){
			if(!set1.contains(ite2.next())){
				isEqual = false;
				break;
			}
		}
		
		return isEqual;
		
	}
	void show2(ResultSet rs){
		try{
			while(rs.next()){
				
				System.out.println(rs.getLong("tsi_tn_id") +" " 
						+  rs.getString("tsi_type")  );
			}
		}catch (SQLException e)
		{
			e.printStackTrace();
		}catch (Exception e){
			e.printStackTrace();
		}
	}
	
	public Set<Long> loadScenicNumIds(){
		String scenicNumIdQuery = "select num_id from c_scenicspot";
		ResultSet numIdResultSet = this.selectSQL(scenicNumIdQuery);
		Set<Long> scenicNumIds=new HashSet<>();
		try {
			while(numIdResultSet.next()){
				scenicNumIds.add(numIdResultSet.getLong("num_id"));
			}
		} catch (SQLException e) {
		}
		return scenicNumIds;
	}
	
	public static void main(String args[]){
		Tmysql t = new Tmysql();
		t.connSQL();
		String s1 = "select ccst_type,cst_id from c_ctrip_scenic_type";
		String s2 = "select tsi_tn_id,tsi_type from t_scenicspot_info";
		String s3 = "select num_id,cst_id from c_scenic_type_mapping";
		
		ResultSet resultSet1 = t.selectSQL(s1);
		ResultSet resultSet2 = t.selectSQL(s2);
		ResultSet resultSet3 = t.selectSQL(s3);
		
		t.show1(resultSet1,resultSet2,resultSet3);
		
		
		//t.show2(resultSet2);
		
		t.deconnSQL();
	}
}
