
all_dirs = dir('psy_features/RA*');

output = [];
for cur_dir = all_dirs'
	cur_dir.name
	train_file=strcat('psy_features/',cur_dir.name,'/train.num')
	test_file=strcat('psy_features/',cur_dir.name,'/test.num')

	train_data = load(train_file);
	test_data = load(test_file);

	train_lables = train_data(:,end);
	train_data_proj = train_data(:,end-2:end-1);

	test_lables = test_data(:,end);
	test_data_proj = test_data(:,end-2:end-1);

	train_data_proj_ds = train_data_proj(train_lables==2,:);
	train_data_proj_ds = train_data_proj_ds(1:1,:);
	train_data_proj_ds = [train_data_proj_ds;train_data_proj(train_lables==1,:)];
	train_data_proj_ds = train_data_proj_ds(1:40,:);
	train_data_proj_ds = [train_data_proj_ds;train_data_proj(train_lables==0,:)];
	train_data_proj_ds = train_data_proj_ds(1:80,:);

	train_lables_ds = train_lables(train_lables==2,:);
	train_lables_ds = train_lables_ds(1:1,:);
	train_lables_ds = [train_lables_ds;train_lables(train_lables==1,:)];
	train_lables_ds = train_lables_ds(1:40,:);
	train_lables_ds = [train_lables_ds;train_lables(train_lables==0,:)];
	train_lables_ds = train_lables_ds(1:80,:);

	train_lables_ds = train_lables_ds==1
	predicted_class = knnclassify(test_data_proj,train_data_proj_ds,train_lables_ds,1);

	
	output = [output; test_lables==1 predicted_class]

	


	
end
